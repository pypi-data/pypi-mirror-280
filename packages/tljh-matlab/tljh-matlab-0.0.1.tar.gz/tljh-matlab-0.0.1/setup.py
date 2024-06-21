# Copyright 2024 The MathWorks, Inc.
from setuptools import setup, find_namespace_packages

setup(
    name="tljh-matlab",
    entry_points={"tljh": ["matlab = tljh_matlab.tljh_matlab"]},
    version="0.0.1",
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    package_data={"tljh_matlab.bash_scripts": ["*.sh"]},
    include_package_data=True,
)
