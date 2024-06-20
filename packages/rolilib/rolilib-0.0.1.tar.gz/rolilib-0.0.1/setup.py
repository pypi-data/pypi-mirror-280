from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = "API Wrapper for Rolimon's"
LONG_DESCRIPTION = "rolilib is an open source API Wrapper for Rolimon's"

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
    install_requires=['requests'],
    keywords=['python', 'api', 'rolimons'],
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)