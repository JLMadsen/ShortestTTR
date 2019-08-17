"""
For installing all the necessary libraries.
"""

import os

libraries = ['pydot', 'matplotlib', 'networkx', 'opencv-python']
pip = 'pip install'

for lib in libraries:
    os.system((pip +" "+ lib))