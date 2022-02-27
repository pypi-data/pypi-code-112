# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['colour_datasets',
 'colour_datasets.examples',
 'colour_datasets.loaders',
 'colour_datasets.loaders.tests',
 'colour_datasets.records',
 'colour_datasets.records.tests',
 'colour_datasets.utilities',
 'colour_datasets.utilities.tests']

package_data = \
{'': ['*'],
 'colour_datasets.loaders.tests': ['resources/*'],
 'colour_datasets.utilities.tests': ['resources/*']}

install_requires = \
['cachetools',
 'colour-science>=0.4.0',
 'imageio>=2,<3',
 'numpy>=1.19,<2',
 'opencv-python>=4,<5',
 'scipy>=1.5,<2',
 'tqdm',
 'typing-extensions>=4,<5',
 'xlrd>=1.2,<2']

extras_require = \
{'development': ['biblib-simple',
                 'black',
                 'coverage!=6.3',
                 'coveralls',
                 'flake8',
                 'flynt',
                 'invoke',
                 'mypy',
                 'pre-commit',
                 'pydata-sphinx-theme',
                 'pydocstyle',
                 'pytest',
                 'pytest-cov',
                 'pyupgrade',
                 'restructuredtext-lint',
                 'sphinx>=4,<5',
                 'sphinxcontrib-bibtex',
                 'toml',
                 'twine'],
 'read-the-docs': ['pydata-sphinx-theme', 'sphinxcontrib-bibtex']}

setup_kwargs = {
    'name': 'colour-datasets',
    'version': '0.2.0',
    'description': 'Colour science datasets for use with Colour',
    'long_description': 'Colour - Datasets\n=================\n\n.. start-badges\n\n|actions| |coveralls| |codacy| |version|\n\n.. |actions| image:: https://img.shields.io/github/workflow/status/colour-science/colour-datasets/Continuous%20Integration%20-%20Quality%20&%20Unit%20Tests?label=actions&logo=github&style=flat-square\n    :target: https://github.com/colour-science/colour-datasets/actions\n    :alt: Develop Build Status\n.. |coveralls| image:: http://img.shields.io/coveralls/colour-science/colour-datasets/develop.svg?style=flat-square\n    :target: https://coveralls.io/r/colour-science/colour-datasets\n    :alt: Coverage Status\n.. |codacy| image:: https://img.shields.io/codacy/grade/83345fbde65545d2a4499f32e72866ed/develop.svg?style=flat-square\n    :target: https://www.codacy.com/app/colour-science/colour-datasets\n    :alt: Code Grade\n.. |version| image:: https://img.shields.io/pypi/v/colour-datasets.svg?style=flat-square\n    :target: https://pypi.org/project/colour-datasets\n    :alt: Package Version\n\n.. end-badges\n\nColour science datasets for use with\n`Colour <https://github.com/colour-science/colour>`__ or any Python package\nmanipulating colours. The datasets are hosted in `Zenodo <https://zenodo.org>`__\nunder the\n`Colour Science - Datasets <https://zenodo.org/communities/colour-science-datasets/>`__\ncommunity.\n\nIt is open source and freely available under the\n`New BSD License <https://opensource.org/licenses/BSD-3-Clause>`__ terms.\n\n.. contents:: **Table of Contents**\n    :backlinks: none\n    :depth: 2\n\n.. sectnum::\n\nFeatures\n--------\n\n**Colour - Datasets** was created to overcome issues encountered frequently\nwhen trying to access or use colour science datasets:\n\n- No straightforward ingestion path for dataset content.\n- No simple loading mechanism for dataset content.\n- Unavailability of the dataset, e.g. download url is down, dataset content is\n  passed directly from hand to hand.\n- No information regarding the definitive origination of the dataset.\n\n**Colour - Datasets** offers all the above: it allows users to ingest and load\ncolour science datasets with a single function call. The datasets information\nis hosted on `Zenodo <https://zenodo.org/communities/colour-science-datasets/>`__\nwhere the record for a dataset typically contain:\n\n- An *urls.txt* file describing the urls to source the dataset files from.\n- A copy of those files in the eventuality where the source files are not\n  available or the content has changed without notice.\n- Information about the authors, content and licensing.\n\nWhen no explicit licensing information is available, the dataset adopts the\n**Other (Not Open)** licensing scheme, implying that assessing usage conditions\nis at the sole discretion of the users.\n\nExamples\n^^^^^^^^\n\n**Colour - Datasets** can also be used online with\n`Google Colab <https://colab.research.google.com/notebook#fileId=1YwIfDTBVP3XUYJAyZVEDWj92DJCB0_3v&offline=true&sandboxMode=true>`__.\n\nMost of the objects are available from the ``colour_datasets`` namespace:\n\n.. code-block:: python\n\n    >>> import colour_datasets\n\nThe available datasets are listed with the ``colour_datasets.datasets()``\ndefinition:\n\n.. code-block:: python\n\n    >>> print(colour_datasets.datasets())\n\n::\n\n    colour-science-datasets\n    =======================\n\n    Datasets : 21\n    Synced   : 1\n    URL      : https://zenodo.org/communities/colour-science-datasets/\n\n    Datasets\n    --------\n\n    [ ] 3269926 : Agfa IT8.7/2 Set - Marszalec (n.d.)\n    [ ] 3245883 : Camera Spectral Sensitivity Database - Jiang et al. (2013)\n    [ ] 3367463 : Constant Hue Loci Data - Hung and Berns (1995)\n    [ ] 3362536 : Constant Perceived-Hue Data - Ebner and Fairchild (1998)\n    [ ] 3270903 : Corresponding-Colour Datasets - Luo and Rhodes (1999)\n    [ ] 3269920 : Forest Colors - Jaaskelainen et al. (1994)\n    [ ] 4394536 : LUTCHI Colour Appearance Data - Luo and Rhodes (1997)\n    [x] 3245875 : Labsphere SRS-99-020 - Labsphere (2019)\n    [ ] 3269924 : Lumber Spectra - Hiltunen (n.d.)\n    [ ] 4051012 : Measured Commercial LED Spectra - Brendel (2020)\n    [ ] 3269918 : Munsell Colors Glossy (All) (Spectrofotometer Measured) - Orava (n.d.)\n    [ ] 3269916 : Munsell Colors Glossy (Spectrofotometer Measured) - Haanpalo (n.d.)\n    [ ] 3269914 : Munsell Colors Matt (AOTF Measured) - Hauta-Kasari (n.d.)\n    [ ] 3269912 : Munsell Colors Matt (Spectrofotometer Measured) - Hauta-Kasari (n.d.)\n    [ ] 3245895 : New Color Specifications for ColorChecker SG and Classic Charts - X-Rite (2016)\n    [ ] 3252742 : Observer Function Database - Asano (2015)\n    [ ] 3269922 : Paper Spectra - Haanpalo (n.d.)\n    [ ] 3372171 : RAW to ACES Utility Data - Dyer et al. (2017)\n    [ ] 4642271 : Spectral Database of Commonly Used Cine Lighting - Karge et al. (2015)\n    [ ] 4297288 : Spectral Sensitivity Database - Zhao et al. (2009)\n    [ ] 4050598 : Spectral Upsampling Coefficient Tables - Jakob and Hanika. (2019)\n\nA ticked checkbox means that the particular dataset has been synced locally.\nA dataset is loaded by using its unique number: *3245895*:\n\n.. code-block:: python\n\n    >>> print(colour_datasets.load(\'3245895\').keys())\n\n::\n\n    Pulling "New Color Specifications for ColorChecker SG and Classic Charts" record content...\n    Downloading "urls.txt" file: 8.19kB [00:01, 5.05kB/s]\n    Downloading "ColorChecker24_After_Nov2014.zip" file: 8.19kB [00:01, 6.52kB/s]\n    Downloading "ColorChecker24_Before_Nov2014.zip" file: 8.19kB [00:01, 7.66kB/s]\n    Downloading "ColorCheckerSG_After_Nov2014.zip" file: 8.19kB [00:01, 7.62kB/s]\n    Downloading "ColorCheckerSG_Before_Nov2014.zip" file: 8.19kB [00:00, 9.39kB/s]\n    Unpacking "/Users/kelsolaar/.colour-science/colour-datasets/3245895/dataset/ColorCheckerSG_Before_Nov2014.zip" archive...\n    Unpacking "/Users/kelsolaar/.colour-science/colour-datasets/3245895/dataset/ColorCheckerSG_After_Nov2014.zip" archive...\n    Unpacking "/Users/kelsolaar/.colour-science/colour-datasets/3245895/dataset/ColorChecker24_After_Nov2014.zip" archive...\n    Unpacking "/Users/kelsolaar/.colour-science/colour-datasets/3245895/dataset/ColorChecker24_Before_Nov2014.zip" archive...\n    odict_keys([\'ColorChecker24 - After November 2014\', \'ColorChecker24 - Before November 2014\', \'ColorCheckerSG - After November 2014\', \'ColorCheckerSG - Before November 2014\'])\n\nAlternatively, a dataset can be loaded by using its full title:\n*New Color Specifications for ColorChecker SG and Classic Chart - X-Rite (2016)s*\n\n.. code-block:: python\n\n    >>> print(colour_datasets.load(\'3245895\').keys())\n    odict_keys([\'ColorChecker24 - After November 2014\', \'ColorChecker24 - Before November 2014\', \'ColorCheckerSG - After November 2014\', \'ColorCheckerSG - Before November 2014\'])\n\nUser Guide\n----------\n\nInstallation\n^^^^^^^^^^^^\n\nPrimary Dependencies\n~~~~~~~~~~~~~~~~~~~~\n\n**Colour - Datasets** requires various dependencies in order to run:\n\n- `python >= 3.8, < 4 <https://www.python.org/download/releases/>`__\n- `cachetools <https://pypi.org/project/cachetools/>`__\n- `colour-science >= 4 <https://pypi.org/project/colour-science/>`__\n- `imageio >= 2, < 3 <https://imageio.github.io/>`__\n- `numpy >= 1.19, < 2 <https://pypi.org/project/numpy/>`__\n- `scipy >= 1.5, < 2 <https://pypi.org/project/scipy/>`__\n- `tqdm <https://pypi.org/project/tqdm/>`__\n- `xlrd <https://pypi.org/project/xlrd/>`__\n\nPypi\n~~~~\n\nOnce the dependencies are satisfied, **Colour - Datasets** can be installed from\nthe `Python Package Index <http://pypi.python.org/pypi/colour-datasets>`__ by\nissuing this command in a shell::\n\n    pip install --user colour-datasets\n\nThe overall development dependencies are installed as follows::\n\n    pip install --user \'colour-datasets[development]\'\n\nContributing\n^^^^^^^^^^^^\n\nIf you would like to contribute to `Colour - Datasets <https://github.com/colour-science/colour-datasets>`__,\nplease refer to the following `Contributing <https://www.colour-science.org/contributing/>`__\nguide for `Colour <https://github.com/colour-science/colour>`__.\n\nBibliography\n^^^^^^^^^^^^\n\nThe bibliography is available in the repository in\n`BibTeX <https://github.com/colour-science/colour-datasets/blob/develop/BIBLIOGRAPHY.bib>`__\nformat.\n\nAPI Reference\n-------------\n\nThe main technical reference for `Colour - Datasets <https://github.com/colour-science/colour-datasets>`__\nis the `API Reference <https://colour-datasets.readthedocs.io/en/latest/reference.html>`__.\n\nCode of Conduct\n---------------\n\nThe *Code of Conduct*, adapted from the `Contributor Covenant 1.4 <https://www.contributor-covenant.org/version/1/4/code-of-conduct.html>`__,\nis available on the `Code of Conduct <https://www.colour-science.org/code-of-conduct/>`__ page.\n\nContact & Social\n----------------\n\nThe *Colour Developers* can be reached via different means:\n\n- `Email <mailto:colour-developers@colour-science.org>`__\n- `Facebook <https://www.facebook.com/python.colour.science>`__\n- `Github Discussions <https://github.com/colour-science/colour-datasets/discussions>`__\n- `Gitter <https://gitter.im/colour-science/colour>`__\n- `Twitter <https://twitter.com/colour_science>`__\n\nAbout\n-----\n\n| **Colour - Datasets** by Colour Developers\n| Copyright 2019 Colour Developers – `colour-developers@colour-science.org <colour-developers@colour-science.org>`__\n| This software is released under terms of New BSD License: https://opensource.org/licenses/BSD-3-Clause\n| `https://github.com/colour-science/colour-datasets <https://github.com/colour-science/colour-datasets>`__\n',
    'author': 'Colour Developers',
    'author_email': 'colour-developers@colour-science.org',
    'maintainer': 'Colour Developers',
    'maintainer_email': 'colour-developers@colour-science.org',
    'url': 'https://www.colour-science.org/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
