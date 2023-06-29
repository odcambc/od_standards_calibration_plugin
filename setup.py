# -*- coding: utf-8 -*-
from __future__ import annotations

from setuptools import find_packages
from setuptools import setup


setup(
    name="od_standards_calibration_plugin",
    version="1.0.2",
    license="MIT",
    description="Calibrate OD using a set of standards.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author_email="christian.macdonald@ucsf.edu",
    author="Chris Macdonald",
    url="https://github.com/odcambc/od_standards_calibration_plugin",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "pioreactor.plugins": "od_standards_calibration_plugin = od_standards_calibration_plugin"
    },
)
