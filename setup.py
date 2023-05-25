#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="DicomView",
    version="1.0",
    description="A simple DICOM viewer in Python",
    author="Julian Loiacono",
    author_email="jcloiacon@gmail.com",
    url="https://github.com/julianfl0w/DicomView",
    packages=find_packages(exclude=("examples")),
    package_data={
        # everything
        # "": ["*"]
        "": ["."]
    },
    include_package_data=True,
)
