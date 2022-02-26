import os
import glob
import sys
import subprocess
from unitgrade_private.autolab.autolab import format_autolab_json
from unitgrade_private.docker_helpers import student_token_file_runner
from unitgrade_private import load_token
import time

verbose = False
tag = "[driver_python.py]"

if not verbose:
    print("="*10)
    print(tag, "Starting unitgrade evaluation...")

sys.stderr = sys.stdout
wdir = os.getcwd()

def pfiles():
    print("> Files in dir:")
    for f in glob.glob(wdir + "/*"):
        print(f)
    print("---")

student_token_file = '{{handin_filename}}'
instructor_grade_script = '{{instructor_grade_file}}'
grade_file_relative_destination = "{{grade_file_relative_destination}}"
host_tmp_dir = wdir + "/tmp"

if not verbose:
    pfiles()
    print(f"{host_tmp_dir=}")
    print(f"{student_token_file=}")
    print(f"{instructor_grade_script=}")

command, token = student_token_file_runner(host_tmp_dir, student_token_file, instructor_grade_script, grade_file_relative_destination)
command = f"cd tmp && {command} --noprogress --autolab"

def rcom(cm):
    rs = subprocess.run(cm, capture_output=True, text=True, shell=True)
    print(rs.stdout)
    if len(rs.stderr) > 0:
        print(tag, "There were errors in executing the file:")
        print(rs.stderr)

start = time.time()
rcom(command)
ls = glob.glob(token)
f = ls[0]
results, _ = load_token(ls[0])

if verbose:
    print(f"{token=}")
    print(results['total'])

format_autolab_json(results)

# if os.path.exists(host_tmp_dir):
#     shutil.rmtree(host_tmp_dir)
# with io.BytesIO(sources['zipfile']) as zb:
#     with zipfile.ZipFile(zb) as zip:
#         zip.extractall(host_tmp_dir
# print("="*10)
# print('{"scores": {"Correctness": 100,  "Problem 1": 4}}')
## Format the scores here.

# sc = [('Total', results['total'][0])] + [(q['title'], q['obtained']) for k, q in results['details'].items()]
# ss = ", ".join([f'"{t}": {s}' for t, s in sc])
# scores = '{"scores": {' + ss + '}}'
# print('{"_presentation": "semantic"}')
# print(scores)

