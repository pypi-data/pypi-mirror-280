"""
Movelets for Multiple Aspect Trajectory Data Mining

The present application offers a tool, to support the user in the classification task of multiple aspect trajectories,
specifically for extracting and visualizing the movelets, the parts of the trajectory that better discriminate a class.
It integrates into a unique platform the fragmented approaches available for multiple aspects trajectories and in
general for multidimensional sequence classification into a unique web-based and python library system. Offers both
movelets visualization and classification methods.

Created on May, 2023
Copyright (C) 2023, License GPL Version 3 or superior (see LICENSE file)

@author: Tarlis Portela
"""
import setuptools

import configparser
config = configparser.ConfigParser()
config.read('pyproject.toml')
VERSION = config['project']['version'].strip('"')
PACKAGE_NAME = config['project']['name'].strip('"')
DEV_VERSION = "0.1b1"

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name=PACKAGE_NAME,
    version=VERSION,
#    version=DEV_VERSION,
    author="Tarlis Tortelli Portela",
    author_email="tarlis@tarlis.com.br",
    description="Movelets for Multiple Aspect Trajectory Data Mining",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ttportela/movelets",
#    packages=setuptools.find_packages(include=[PACKAGE_NAME, PACKAGE_NAME+'.*']),
    packages=setuptools.find_packages(),
#    include_package_data=True,
    scripts=[
        'scripts/MAT-Web.py',
        
        'scripts/results/MAT-Summary.py',
        'scripts/results/MAT-ExportResults.py',
        'scripts/results/MAT-PrintResults.py',
        'scripts/results/MAT-MoveResults.py',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    keywords='data mining, python, trajectory classification, trajectory analysis, movelets',
    license='GPL Version 3 or superior (see LICENSE file)',
)
