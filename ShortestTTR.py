import cv2, time, pydot, sys

import networkx as nx
from networkx.drawing.nx_pydot import write_dot

import matplotlib.pyplot as plt
from itertools import permutations

from src.Dijkstra import dijkstra
from src.Board import Board

graph = {}
pos = {}
board = Board()
G = nx.Graph()

def saveImage():
    # get color
    edges = G.edges()
    colors = [G[u][v]['color'] for u,v in edges]
    widths = [G[u][v]['width'] for u,v in edges]

    # draw graph
    #font_color='b'
    nx.draw(G, pos, edges=edges, edge_color=colors, width=widths, with_labels=True)

    # save to root dir as png
    plt.savefig("Graph.png")
    
    # clear image to prevent overlap
    plt.clf()

# TODO: check deeper cul de sac's and fix them
# CUrrent implementation only finds them.
def cul_de_sac(path):
    
    nodes = []
    
    for i in range(len(path)-1):
        for j in range(i+1, len(path)):
            if path[i] == path[j]:
                nodes.append(path[i])
    
    print("nodes visited more than once:")
    print(nodes)

def drawImage():
    # read image and show
    img = cv2.imread('Graph.png', 1)
    cv2.imshow('image', img)
    cv2.waitKey(1)

def closeWindows():
    cv2.destroyAllWindows()

def update():
    saveImage()
    drawImage()

def visualizePath(G, path):
    # make path red
    for i in range(len(path)-1):
        G.add_edge(path[i], path[i+1], color='r', width=4.0)

    # draw new path and pause
    update()
    time.sleep(0.5)

    # make path normal again
    for i in range(len(path)-1):
        G.add_edge(path[i], path[i+1], color='g', width=2.0)

# homemade bool refers to using my dijkstra algorithm or the NetworkX dijkstra
def tryPath(homemade, perm):
    
    # paths are all the seperate paths between nodes, eg. Edinburgh -> Sochi, Sochi -> Stockholm
    paths = []
    weight = 0

    if homemade:
        # get path between nodes using homemade dijkstra
        for i in range(len(perm)-1):
            print("using homemade")
            paths, weight = dijkstra(graph, perm[i], perm[i+1])
            paths.append(paths)
    else:
        # get path between nodes using nx dijkstra
        for i in range(len(perm)-1):
            paths.append(nx.dijkstra_path(G, perm[i], perm[i+1]))

    # unfiy all paths into one path
    path = []
    for i in range(len(paths)):
        if i == 0:
            for node in paths[i]:
                path.append(node)
                continue
        if path[-1] == paths[i][0]:
            for node in paths[i][1:]:
                path.append(node)
                
    # if using nx dijkstra i need to calculate the weight manualy
    if not homemade:           
        # get weight for path
        for i in range(len(path)-1):
            try:
                weight += graph[path[i]][path[i+1]]
            except TypeError:
                exit("Wrong list format on:\n"+ str(path))

    return path, weight

# probably not necessarry
def getMaps():
    return board.getMaps()

def getNodes(mapName):
    graph, pos = board.getMap(mapName)
    return graph.keys()

def MapAndGoals(sysArgv):
    
    if(sysArgv):
        # Enter map name, then goals, seperated by spaces.
        mapName = sys.argv[1]
        goals = sys.argv[2:]
    else:
        print("Enter map name")
        mapName = input()
        print("Enter goals, seperate with space.")
        goals = input().split(" ")

    global graph
    global pos
    
    graph, pos = board.getMap(mapName)
    if not goals or len(goals) == 1:
        exit("Not enough goals.")

def main():
    # input method
    sysArgv = False
    MapAndGoals(sysArgv)
    
    # add nodes, 47 total
    G.add_nodes_from(graph.keys())

    # add edges, 180 total
    for node1, edges in graph.items():
        for node2, weight in edges.items():
            if not G.has_edge(node1, node2) or not G.has_edge(node2, node1): # skip duplicates
                G.add_edge(node1, node2, weight=weight, color='g', width=2.0)

    update()
    time.sleep(1)

    # permutate goals
    perms = list(permutations(goals))

    # get rid of reversed copies
    for i in range(len(perms)-1):
        for j in range(i, len(perms)-1):
            if perms[j] == perms[i][::-1]:
                perms.pop(j)

    # try each permutated path
    routes = []
    for perm in perms:
        path, weight = tryPath(False, perm)
        routes.append([path, weight])

    # visualize all the permutated paths, after this the weights are removed from the edges
    for path, weight in routes:
        visualizePath(G, path)
    
    # find shortest permutated path
    lowest = 0
    for i in range(len(routes)):
        if routes[i][1] < routes[lowest][1]:
            lowest = i

    path, weight = routes[lowest]
    visualizePath(G, path)
    print(path, weight)
    cul_de_sac(path)
    
    # pause to see image
    time.sleep(4) 
    
    closeWindows()
    exit("Closing...")
    
if __name__ == '__main__':
    main()
