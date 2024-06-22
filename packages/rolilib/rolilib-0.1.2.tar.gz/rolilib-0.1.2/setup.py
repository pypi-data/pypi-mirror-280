from setuptools import setup, find_packages
from pathlib import Path
import codecs
import os

VERSION = '0.1.2'
DESCRIPTION = "API Wrapper for Rolimon's"
this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()   # "rolilib is an open source API Wrapper for Rolimon's"

# Setting up
setup(
    name="rolilib",
    version=VERSION,
    author="ThunderFound",
    author_email="<contact.thunderfound@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests', 'datetime'],
    keywords=['python', 'api', 'rolimons'],
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)