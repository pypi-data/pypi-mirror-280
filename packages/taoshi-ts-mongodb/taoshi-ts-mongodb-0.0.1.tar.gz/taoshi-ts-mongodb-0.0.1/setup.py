import os
from setuptools import setup

with open("README.md") as description_file:
    long_description = description_file.read()

setup(
    name=os.environ["TAOSHI_TS_PACKAGE_NAME"],
    version="0.0.1",
    author="Taoshi Inc",
    author_email="python@taoshi.io",
    url="https://taoshi.io/",
    description="This package name is reserved by Taoshi Inc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["taoshi"],
    install_requires=[],
)
