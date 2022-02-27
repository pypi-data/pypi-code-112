#!/usr/bin/python

# pip install lxml

import sys
import os
import json
import xml.etree.ElementTree as ET
import glob
from tqdm import tqdm

START_BOUNDING_BOX_ID = 1
PRE_DEFINE_CATEGORIES = None
# If necessary, pre-define category and its id
#  PRE_DEFINE_CATEGORIES = {"aeroplane": 1, "bicycle": 2, "bird": 3, "boat": 4,
#  "bottle":5, "bus": 6, "car": 7, "cat": 8, "chair": 9,
#  "cow": 10, "diningtable": 11, "dog": 12, "horse": 13,
#  "motorbike": 14, "person": 15, "pottedplant": 16,
#  "sheep": 17, "sofa": 18, "train": 19, "tvmonitor": 20}


def get(root, name):
    vars = root.findall(name)
    return vars


def get_and_check(root, name, length):
    vars = root.findall(name)
    if len(vars) == 0:
        raise ValueError("Can not find %s in %s." % (name, root.tag))
    if length > 0 and len(vars) != length:
        raise ValueError(
            "The size of %s is supposed to be %d, but is %d." % (name, length, len(vars))
        )
    if length == 1:
        vars = vars[0]
    return vars


def get_filename_as_int(filename):
    try:
        filename = filename.replace("\\", "/")
        filename = os.path.splitext(os.path.basename(filename))[0]
        return int(filename)
    except:
        raise ValueError("Filename %s is supposed to be an integer." % (filename))


class image_id_create:
    def __init__(self):
        self.image_id_map = dict()
        self.all_images = list()

    def add_image(self, file_name):
        isin = file_name in self.image_id_map
        if not isin:
            self.all_images.append(file_name)
            int_label = self.all_images.index(file_name)
            self.image_id_map[file_name] = int_label

    def get_filename_as_int(self, filename):
        return self.image_id_map[filename]


def get_categories(xml_files):
    """Generate category name to id mapping from a list of xml files.
    
    Arguments:
        xml_files {list} -- A list of xml file paths.
    
    Returns:
        dict -- category name to id mapping.
    """
    classes_names = []
    for xml_file in xml_files:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall("object"):
            classes_names.append(member[0].text)
    classes_names = list(set(classes_names))
    classes_names.sort()
    return {name: i for i, name in enumerate(classes_names)}


def convert(xml_dir, json_file, origin_file_name=False):
    xml_files = glob.glob(os.path.join(xml_dir, "*.xml"))
    # If you want to do train/test split, you can pass a subset of xml files to convert function.
    print("Number of xml files: {}".format(len(xml_files)))

    json_dict = {"images": [], "type": "instances", "annotations": [], "categories": []}
    iic = image_id_create()

    if PRE_DEFINE_CATEGORIES is not None:
        categories = PRE_DEFINE_CATEGORIES
    else:
        categories = get_categories(xml_files)
    bnd_id = START_BOUNDING_BOX_ID
    for xml_file in tqdm(xml_files):

        tree = ET.parse(xml_file)
        root = tree.getroot()
        if origin_file_name:
            path = get(root, "path")
            if len(path) == 1:
                filename = os.path.basename(path[0].text)
            elif len(path) == 0:
                filename = get_and_check(root, "filename", 1).text
            else:
                raise ValueError("%d paths found in %s" % (len(path), xml_file))
        else:
            filename = xml_file.split(os.sep)[-1].split('.')[0]

        # Modified image id function
        iic.add_image(filename)
        image_id = iic.get_filename_as_int(filename)
        #         ## The filename must be a number
        #         image_id = get_filename_as_int(filename)
        size = get_and_check(root, "size", 1)
        width = int(get_and_check(size, "width", 1).text)
        height = int(get_and_check(size, "height", 1).text)
        image = {
            "file_name": filename,
            "height": height,
            "width": width,
            "id": image_id,
        }
        json_dict["images"].append(image)
        ## Currently we do not support segmentation.
        #  segmented = get_and_check(root, 'segmented', 1).text
        #  assert segmented == '0'
        for obj in get(root, "object"):
            category = get_and_check(obj, "name", 1).text
            if category not in categories:
                new_id = len(categories)
                categories[category] = new_id
            category_id = categories[category]
            bndbox = get_and_check(obj, "bndbox", 1)
            xmin = int(float(get_and_check(bndbox, "xmin", 1).text)) - 1
            ymin = int(float(get_and_check(bndbox, "ymin", 1).text)) - 1
            xmax = int(float(get_and_check(bndbox, "xmax", 1).text))
            ymax = int(float(get_and_check(bndbox, "ymax", 1).text))
            assert xmax > xmin
            assert ymax > ymin
            o_width = abs(xmax - xmin)
            o_height = abs(ymax - ymin)
            ann = {
                "area": o_width * o_height,
                "iscrowd": 0,
                "image_id": image_id,
                "bbox": [xmin, ymin, o_width, o_height],
                "category_id": category_id,
                "id": bnd_id,
                "ignore": 0,
                "segmentation": [],
            }
            json_dict["annotations"].append(ann)
            bnd_id = bnd_id + 1

    for cate, cid in categories.items():
        cat = {"supercategory": "none", "id": cid, "name": cate}
        json_dict["categories"].append(cat)

    os.makedirs(os.path.dirname(json_file), exist_ok=True)
    json_fp = open(json_file, "w")
    json_str = json.dumps(json_dict)
    json_fp.write(json_str)
    json_fp.close()
    print("Success: {}".format(json_file))


# usage
# where train is the folder contains xml files, the output json will be under train/ dir
# convert('train', 'train/train_annotations.json', origin_file_name=False)
