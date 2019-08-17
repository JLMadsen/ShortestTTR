#!/usr/bin/python3

"""
This script is used to create maps and positions, it makes it easy by printing the dictionary so i can paste it into Boards.py.

To use this just run it and enter "node1 node2 x"
This will create node1 key and link it to node 2 with int(x) as the weight.
Also connects node2 to node1 with the same weight.

If not graphing:
Enter node, x, y.
Easist way is to slap a grid on the map and number it.
Scale doesnt matter because numbers dont mean much, only need relative positions.
"""

graph = {}
pos = {}

print("Graph? if not graph enter positions (Y/N)")
graphing = if input().lower() == 'y'

while True:
    
    if graphing:
        node1, node2, weight = input().split(" ")
        if node1 == '*':
            break
            
        weight = int(weight)
        
        if node1 not in graph:
            graph[node1] = {}
        if node2 not in graph:
            graph[node2] = {}
            
        graph[node1][node2] = weight
        graph[node2][node1] = weight
    else:
        node, x, y = input().split(" ")
        x, y = int(x), int(y)
        
        pos[node] = (x, y)
    
if graphing:
    print(graph)
else:
    print(pos)
