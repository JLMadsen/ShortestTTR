#!/usr/bin/python3

"""
For installing all the necessary libraries.

Libraries:
Pydot
Matplotlib
NetworkX
OpenCV

"""

import os

libraries = ['pydot', 'matplotlib', 'networkx', 'opencv-python']
pip = 'pip install'

for lib in libraries:
    os.system((pip +" "+ lib))