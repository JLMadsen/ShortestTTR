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

from Board import Board

board = Board()
graph = {}
pos = {}

def reversePos(mapName, side, n):
    ra = list(range(1, n+1))
    graph, pos = board.getMap(mapName)
    if side:
        for x, y in pos.values():
            new = ra[::-1][ra.index(x)]
            print(x, '->', new)
            x = new
    else:
        for node in pos.keys():
            x, y = pos[node]
            new = ra[::-1][ra.index(y)]
            print(y, '->', new)
            pos[node] = (x, new)

    print(pos)

print("Graph? if not graph enter positions (Y/N)")
graphing = input().lower()

# for reverting positions
if graphing == 'r':
    print("map?")
    mapName = input().capitalize()
    print("x or y?")
    x = input().lower()
    if x == 'x':
        x = True
    else:
        x = False
    print('Range?')
    n = int(input())
    reversePos(mapName, x, n)
    exit()

if graphing[0] == 'y':
    graphing = True
else:
    graphing = False

while graphing:
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


if not graphing:
    print('which map?')
    mapName = input()
    graph, pos = board.getMap(mapName)
    for node in graph.keys():
        print(node) 
        x, y = input().split(" ")
        x, y = int(x), int(y)    
        pos[node] = (x, y)
    
if graphing:
    print(graph)
else:
    print(pos)
