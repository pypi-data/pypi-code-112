#!/Users/jss009/code/test_gh_actions/venv/bin/python

import yaml
import json
import sys

yaml_schema = yaml.load(sys.stdin, Loader=yaml.SafeLoader)
json.dump(yaml_schema, sys.stdout, indent=3)
