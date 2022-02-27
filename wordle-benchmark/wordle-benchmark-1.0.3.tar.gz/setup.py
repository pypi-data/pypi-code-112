"""
Call "pip install ." to initialize
Call "pip install -e ." for local development, see also requirements.txt
"""

import pathlib
import setuptools

README = (
    pathlib.Path(__file__).parent / "README.md"  # pylint: disable=unspecified-encoding
).read_text()

setuptools.setup(
    name="wordle-benchmark",
    version="1.0.3",
    description="Wordle package to benchmark agents. The package is intended \
        to support replicable heuristic evaluation of Wordle playing software.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Peter Bryan",
    author_email="peterbbryan@gmail.com",
    license="MIT",
    python_requires=">3.7",
    packages=setuptools.find_packages(),
    install_requires=["numpy", "requests"],
)
