import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="TOPSIS-Divya-101953024",
    version="1.0.1",
    description="TOPSIS",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Divya Goel",
    author_email="divyaji.goel@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["TOPSIS"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "TOPSIS=TOPSIS.__main__:main",
        ]
    },
)
