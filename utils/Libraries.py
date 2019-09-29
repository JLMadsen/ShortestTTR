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

# update pip
os.system("pip install --upgrade pip")

for lib in libraries:
    os.system((pip +" "+ lib))