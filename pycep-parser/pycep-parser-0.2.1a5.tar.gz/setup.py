# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycep']

package_data = \
{'': ['*']}

install_requires = \
['lark>=1.1.1,<2.0.0',
 'regex>=2022.1.18,<2023.0.0',
 'typing-extensions>=4.1.1,<5.0.0']

setup_kwargs = {
    'name': 'pycep-parser',
    'version': '0.2.1a5',
    'description': 'A Python based Bicep parser',
    'long_description': '# pycep\n\n[![Build Status](https://github.com/gruebel/pycep/workflows/CI/badge.svg)](https://github.com/gruebel/pycep/actions)\n[![codecov](https://codecov.io/gh/gruebel/pycep/branch/master/graph/badge.svg?token=49WHVYGE1D)](https://codecov.io/gh/gruebel/pycep)\n[![PyPI](https://img.shields.io/pypi/v/pycep-parser)](https://pypi.org/project/pycep-parser/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pycep-parser)](https://github.com/gruebel/pycep)\n![CodeQL](https://github.com/gruebel/pycep/workflows/CodeQL/badge.svg)\n\nA fun little project, which has the goal to parse\n[Azure Bicep](https://github.com/Azure/bicep) files.\nThis is still a very early stage, therefore a lot can and will change.\n\n## Current capabalities\n\n[Supported capabilities](docs/capabilities.md)\n\n## Next milestones\n\n### General\n- [x] Complete loop support\n- [x] Param decorator\n- [x] Resource/Module decorator\n- [x] Target scope\n- [x] Existing resource keyword\n- [x] Child resources\n- [ ] Module alias\n- [x] Deployment condition\n- [x] Adding line numbers to element blocks\n\n### Functions\n- [x] Any\n- [ ] Array (in progress)\n- [x] Date\n- [x] Deployment\n- [ ] File\n- [x] Logical\n- [x] Numeric\n- [x] Object\n- [x] Resource\n- [x] Scope\n- [ ] String (in progress)\n\n### Operators\n- [ ] Accessor\n- [x] Numeric\n\n### CI/CD\n- [ ] Fix security issues found by Scorecard\n\n## Considering\n- Adding line numbers to other parts\n\n## Out-of-scope\n- Bicep to ARM converter and vice versa\n',
    'author': 'Anton Grübel',
    'author_email': 'anton.gruebel@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/gruebel/pycep',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
