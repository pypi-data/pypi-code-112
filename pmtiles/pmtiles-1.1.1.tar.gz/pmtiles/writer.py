import gzip
import itertools
import json
from contextlib import contextmanager
from collections import defaultdict

def tilesort(t):
    return (t[0],t[1],t[2])

@contextmanager
def write(fname):
    w = Writer(fname)
    try:
        yield w
    finally:
        w.close()

class Writer:
    def __init__(self,fname):
        self.f = open(fname,'wb')
        self.offset = 512000
        self.f.write(b'\0' * self.offset)
        self.tiles = []
        self.hash_to_offset = {}
        self.leaves = []
        self.zoom_counts = defaultdict(int)

    def write_tile(self,z,x,y,data):
        hsh = hash(data)
        if hsh in self.hash_to_offset:
            self.tiles.append((z,x,y,self.hash_to_offset[hsh],len(data)))
        else:
            self.f.write(data)
            # TODO optimize order
            self.tiles.append((z,x,y,self.offset,len(data)))
            self.hash_to_offset[hsh] = self.offset
            self.offset = self.offset + len(data)
            self.zoom_counts[z] += 1

    def write_entry(self,entry):
        self.f.write(entry[0].to_bytes(1,byteorder='little'))
        self.f.write(entry[1].to_bytes(3,byteorder='little'))
        self.f.write(entry[2].to_bytes(3,byteorder='little'))
        self.f.write(entry[3].to_bytes(6,byteorder='little'))
        self.f.write(entry[4].to_bytes(4,byteorder='little'))

    def write_leafdir(self,tiles,total_len):
        entries_to_sort = []
        for t in tiles:
            self.leaves.append((t[0][0],t[0][1],t[0][2],self.offset,17*total_len))
            entries = t[1]
            for entry in entries:
                entries_to_sort.append(entry)
        entries_to_sort.sort(key=tilesort)
        for entry in entries_to_sort:
                self.write_entry(entry)

    def write_header(self,metadata,root_entries_len):
        self.f.write((0x4D50).to_bytes(2,byteorder='little'))
        self.f.write((2).to_bytes(2,byteorder='little'))
        metadata_serialized = json.dumps(metadata)
        # 512000 - (17 * 21845) - 2 (magic) - 2 (version) - 4 (jsonlen) - 2 (dictentries) = 140625
        assert len(metadata_serialized) < 140625
        self.f.write(len(metadata_serialized).to_bytes(4,byteorder='little'))
        self.f.write(root_entries_len.to_bytes(2,byteorder='little'))
        self.f.write(metadata_serialized.encode('utf-8'))


    def finalize(self,metadata = {}):
        if len(self.tiles) < 21845:
            self.f.seek(0)
            self.write_header(metadata,len(self.tiles))
            self.tiles.sort(key=tilesort)
            for entry in self.tiles:
                self.write_entry(entry)
        else:
            leafdir_tiles = []
            leafdir_len = 0

            # Find best base zoom to avoid extra indirection for as many tiles as we can
            base_zoom = 7
            n_so_far = sum(self.zoom_counts[z] for z in range(0,8))
            while n_so_far + self.zoom_counts[base_zoom+1] < 21845:
                n_so_far += self.zoom_counts[base_zoom+1]
                base_zoom += 1

            def by_parent(t):
                if t[0] >= base_zoom:
                    level_diff = t[0] - base_zoom
                    return (base_zoom,t[1]//(1 << level_diff),t[2]//(1 << level_diff))
                else:
                    return (0,t[1]//(1 << t[0]),t[2]//(1 << t[0]))

            # TODO optimize order
            self.tiles.sort(key=by_parent)
            for group in itertools.groupby(self.tiles,key=by_parent):
                if group[0][0] != base_zoom:
                    continue
                entries = list(group[1])
                if leafdir_len + len(entries) <= 21845:
                    leafdir_tiles.append((group[0],entries))
                    leafdir_len = leafdir_len + len(entries)
                else:
                    self.write_leafdir(leafdir_tiles,leafdir_len)
                    self.offset += 17 * leafdir_len
                    leafdir_tiles = [(group[0],entries)]
                    leafdir_len = len(entries)

            # finalize
            if len(leafdir_tiles):
                self.write_leafdir(leafdir_tiles,leafdir_len)

            root_tiles = []
            root = [(group[0],list(group[1])) for group in itertools.groupby(self.tiles,key=by_parent) if group[0][0] == 0]
            if root:
                root_tiles = root[0][1]
            self.f.seek(0)
            self.write_header(metadata,len(root_tiles) + len(self.leaves))
            root_tiles.sort(key=tilesort)
            for entry in root_tiles:
                self.write_entry(entry)

            # the leaf level > the root tile entries
            self.leaves.sort(key=tilesort)
            for entry in self.leaves:
                z_dir = (0b10000000 | entry[0])
                self.write_entry((z_dir,entry[1],entry[2],entry[3],entry[4]))

        return {'num_tiles':len(self.tiles),'num_unique_tiles':len(self.hash_to_offset),'num_leaves':len(self.leaves)}

    def close(self):
        self.f.close()
