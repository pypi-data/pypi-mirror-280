#!python
# -*- coding: utf-8 -*-
'''
# MAT-tools: Tools for Multiple Aspect Trajectory Data Mining \[MAT-Tools Framework\]

The present application offers a set of tools, to support the user in the data mining and analysis tasks for multiple aspect trajectories. It integrates into a unique platform the fragmented approaches available for multiple aspects trajectories and in general for multidimensional sequence classification into a unique web-based and python library system.

Created on Dec, 2023
Copyright (C) 2023+, License GPL Version 3 or superior (see LICENSE file)
'''
import sys, os 
sys.path.insert(0, os.path.abspath('.'))

import argparse

def parse_args():
    """[This is a function used to parse command line arguments]

    Returns:
        args ([object]): [Parse parameter object to get parse object]
    """
    parse = argparse.ArgumentParser(description='MAT Web')
    parse.add_argument('-d', '--data', '--data-path', type=str, default='../sample', help='path for the datasets folder (for listing)')
    
    args = parse.parse_args()
    config = vars(args)
    return config
 
config = parse_args()
#print(config)

data_path  = config["data"]
#experiment_path  = config["experiment-path"]

# UNDER CONSTRUCTION
from matview.web.app import app
from matview.web.config import HOST, PORT, DEBUG

os.environ['MATVIEW_DATA_PATH'] = data_path

app.run_server(host=HOST, port=PORT, debug=DEBUG)

