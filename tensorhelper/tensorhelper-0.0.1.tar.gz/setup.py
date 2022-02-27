from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A helper function for data analytics and machine learning'
LONG_DESCRIPTION = 'A package that loads random images from a directory, a custom built confusion matrix and generate accuracy and loss curves for machine learning'

# Setting up
setup(
    name="tensorhelper",
    version=VERSION,
    author="ifeanyi_omeck",
    author_email="kifeanyi@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'matplotlib', 'tensorflow'],
    keywords=['python', 'confusion_matrix', 'loss_curves', 'accuracy_curves', 'random_images'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)