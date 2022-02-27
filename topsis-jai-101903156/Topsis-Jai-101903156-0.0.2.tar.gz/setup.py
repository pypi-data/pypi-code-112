from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2'
DESCRIPTION = "Topsis score calculator"
LONG_DESCRIPTION = "TOPSIS is Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) originated in the 1980s as a multi-criteria decision making method. TOPSIS chooses the alternative of shortest Euclidean distance from the ideal solution, and greatest distance from the negative-ideal solution.Include the module at the top of your python code as follows:from Topsis_Jai_101903156.topsis import *.Then use the function topsis_score('csv path or filename if the code and dataset are in the same directory','comma separated weights','comma separated impacts','name_of_result_file.csv').Run the code and you will get a csv file as your result containing topsis score and ranks"

# Setting up
setup(
    name="Topsis-Jai-101903156",
    version=VERSION,
    author="Jai Singh Batth",
    author_email="batthjaisingh2000@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'topsis', '101903156', 'JaiSinghBatth'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)