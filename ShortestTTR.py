import networkx as nx
from networkx.drawing.nx_pydot import write_dot
import matplotlib.pyplot as plt
import cv2, time, pydot
from itertools import permutations

graph = {'Edinburgh': {'London': 4}, 'London': {'Edinburgh': 4, 'Dieppe': 2, 'Amsterdam': 2}, 'Dieppe': {'London': 2, 'Brest': 2, 'Paris': 1, 'Bruxelles': 2}, 'Brest': {'Dieppe': 2, 'Pamplona': 4, 'Paris': 3}, 'Pamplona': {'Brest': 4, 'Madrid': 3, 'Barcelona': 2, 'Marseille': 4, 'Paris': 4}, 'Paris': {'Brest': 3, 'Dieppe': 1, 'Pamplona': 4, 'Marseille': 4, 'Bruxelles': 2, 'Zurich': 3, 'Frankfurt': 3}, 'Bruxelles': {'Dieppe': 2, 'Amsterdam': 1, 'Paris': 2, 'Frankfurt': 2}, 'Amsterdam': {'London': 2, 'Bruxelles': 1, 'Essen': 3, 'Frankfurt': 2}, 'Madrid': {'Pamplona': 3, 'Lisboa': 3, 'Cadiz': 3, 'Barcelona': 2}, 'Lisboa': {'Madrid': 3, 'Cadiz': 2}, 'Cadiz': {'Lisboa': 2, 'Madrid': 3}, 'Barcelona': {'Madrid': 2, 'Pamplona': 2, 'Marseille': 4}, 'Marseille': {'Barcelona': 4, 'Pamplona': 4, 'Paris': 4, 'Zurich': 2, 'Roma': 4}, 'Zurich': {'Paris': 3, 'Marseille': 2, 'Munchen': 2, 'Venezia': 2}, 'Frankfurt': {'Paris': 3, 'Amsterdam': 2, 'Bruxelles': 2, 'Munchen': 2, 'Essen': 2, 'Berlin': 3}, 'Essen': {'Amsterdam': 3, 'Kobenhavn': 3, 'Berlin': 2, 'Frankfurt': 2}, 'Munchen': {'Frankfurt': 2, 'Zurich': 2, 'Venezia': 2, 'Wien': 3}, 'Venezia': {'Zurich': 2, 'Roma': 2, 'Munchen': 2, 'Zagrab': 2}, 'Roma': {'Marseille': 4, 'Venezia': 2, 'Palermo': 4, 'Brindisi': 2}, 'Palermo': {'Roma': 4, 'Brindisi': 3, 'Smyrna': 6}, 'Brindisi': {'Roma': 2, 'Palermo': 3, 'Athina': 4}, 'Kobenhavn': {'Essen': 3, 'Stockholm': 3}, 'Berlin': {'Essen': 2, 'Frankfurt': 3, 'Danzig': 4, 'Warzawa': 4, 'Wien': 3}, 'Stockholm': {'Kobenhavn': 3, 'Petrograd': 8}, 'Petrograd': {'Stockholm': 8, 'Riga': 4, 'Wilno': 4, 'Moskva': 4}, 'Danzig': {'Berlin': 4, 'Riga': 3, 'Warzawa': 2}, 'Warzawa': {'Berlin': 4, 'Wien': 4, 'Danzig': 2, 'Wilno': 3, 'Kyiv': 4}, 'Wien': {'Berlin': 3, 'Munchen': 3, 'Zagrab': 2, 'Warzawa': 4, 'Budapest': 1}, 'Zagrab': {'Venezia': 2, 'Wien': 2, 'Budapest': 2, 'Sarajevo': 3}, 'Budapest': {'Wien': 1, 'Zagrab': 2, 'Sarajevo': 3, 'Bucuresti': 4, 'Kyiv': 6}, 'Riga': {'Danzig': 3, 'Petrograd': 4, 'Wilno': 4}, 'Wilno': {'Riga': 4, 'Warzawa': 3, 'Petrograd': 4, 'Smolensk': 3, 'Kyiv': 2}, 'Moskva': {'Petrograd': 4, 'Smolensk': 2, 'Kharkov': 4}, 'Smolensk': {'Wilno': 3, 'Moskva': 2, 'Kyiv': 3}, 'Kyiv': {'Wilno': 2, 'Budapest': 6, 'Warzawa': 4, 'Smolensk': 3, 'Bucuresti': 4, 'Kharkov': 4}, 'Smyrna': {'Palermo': 6, 'Athina': 2, 'Constantinople': 2, 'Angora': 3}, 'Athina': {'Brindisi': 4, 'Sarajevo': 4, 'Sofia': 3, 'Smyrna': 2}, 'Sarajevo': {'Zagrab': 3, 'Athina': 4, 'Budapest': 3, 'Sofia': 2}, 'Sofia': {'Sarajevo': 2, 'Athina': 3, 'Bucuresti': 2, 'Constantinople': 3}, 'Bucuresti': {'Budapest': 4, 'Sofia': 2, 'Kyiv': 4, 'Constantinople': 3, 'Sevastapol': 4}, 'Constantinople': {'Sofia': 3, 'Bucuresti': 3, 'Smyrna': 2, 'Sevastapol': 4, 'Angora': 2}, 'Sevastapol': {'Bucuresti': 4, 'Constantinople': 4, 'Rostov': 4, 'Sochi': 2, 'Erzurum': 4}, 'Kharkov': {'Kyiv': 4, 'Moskva': 4, 'Rostov': 2}, 'Rostov': {'Kharkov': 2, 'Sevastapol': 4, 'Sochi': 2}, 'Sochi': {'Sevastapol': 2, 'Rostov': 2, 'Erzurum': 3}, 'Erzurum': {'Sochi': 3, 'Sevastapol': 4, 'Angora': 3}, 'Angora': {'Erzurum': 3, 'Constantinople': 2, 'Smyrna': 3}}
pos = {'Edinburgh': (3, 13), 'London': (4, 10), 'Dieppe': (4, 8), 'Brest': (2, 8), 'Pamplona': (4, 4), 'Paris': (5, 7), 'Bruxelles': (6, 9), 'Amsterdam': (6, 10), 'Madrid': (2, 3), 'Lisboa': (1, 2), 'Cadiz': (2, 1), 'Barcelona': (4, 2), 'Marseille': (7, 4), 'Zurich': (7, 6), 'Frankfurt': (7, 8), 'Essen': (8, 9), 'Munchen': (9, 7), 'Venezia': (9, 5), 'Roma': (9, 3), 'Palermo': (10, 1), 'Brindisi': (11, 3), 'Kobenhavn': (9, 11), 'Berlin': (10, 9), 'Stockholm': (11, 13), 'Petrograd': (17, 12), 'Danzig': (12, 10), 'Warzawa': (13, 9), 'Wien': (11, 7), 'Zagrab': (11, 5), 'Budapest': (12, 6), 'Riga': (14, 12), 'Wilno': (15, 10), 'Moskva': (19, 10), 'Smolensk': (17, 9), 'Kyiv': (16, 8), 'Smyrna': (15, 1), 'Athina': (13, 2), 'Sarajevo': (12, 4), 'Sofia': (14, 4), 'Bucuresti': (15, 5), 'Constantinople': (16, 3), 'Sevastapol': (17, 5), 'Kharkov': (18, 7), 'Rostov': (19, 6), 'Sochi': (19, 4), 'Erzurum': (19, 2), 'Angora': (17, 2)}
G = nx.Graph()

def saveImage():
    # get color
    edges = G.edges()
    colors = [G[u][v]['color'] for u,v in edges]
    widths = [G[u][v]['width'] for u,v in edges]

    # draw graph
    nx.draw(G, pos, edges=edges, edge_color=colors, width=widths, with_labels=True)
    #nx.draw(G)

    # save to root dir as png
    plt.savefig("Graph.png")
    
    # clear image to prevent overlap
    plt.clf()

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


def tryPath(G, perm):
    # paths are all the seperate paths between nodes, eg. einburg -> Sochi, Sochi -> Stockholm
    paths = []
    weight = 0

    # get path between nodes
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
        #else:
        #    exit("Path start does not match previous path end:"+ paths[i][0] +"!="+ path[-1])

    # get weight for path
    for i in range(len(path)-1):
        weight += graph[path[i]][path[i+1]]

    return path, weight

if __name__ == '__main__':
    # all nodes in you paths, change to input l8r
    goals = input().split(" ")
    for i in range(len(goals)):
        goals[i] = goals[i].capitalize()

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
        path, weight = tryPath(G, perm)
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
    
    time.sleep(4) # pause to see image
    closeWindows()
    exit()