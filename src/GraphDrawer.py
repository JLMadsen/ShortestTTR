import cv2, time, pydot, sys
import networkx as nx
import matplotlib.pyplot as plt

from networkx.drawing.nx_pydot import write_dot
from itertools import permutations

"""
Class for drawing graphs easier.
Already exists but i wanted to make my own.
"""

class GraphDrawer:
        
    def __init__(self, directional = False, graph = None) -> None:
        
        if directional:
            self.graph = nx.DiGraph(incoming_graph_data=graph)
        else:
            self.graph = nx.Graph(incoming_graph_data=graph)
            
        self.filename = "Graph.png"
        self.colors = [] #[G[u][v]['color'] for u,v in edges]
        
    def visualizePath(self, node1, node2, color="red") -> None:
        
        self.graph.add_edge(node1, node2, color)
        
    def visualizePath(self, nodes, color="red") -> None:
        
        for i in range(len(nodes)-1):
            self.graph.add_edge(nodes[i], nodes[i+1], color)
            
    def show(self):
        
        nx.draw(self.graph)
        
    def addEgde(self, node1, node2, color="black") -> None:
        
        self.graph.add_edge(node1, node2, edge_color=color)
    
    def addEgde(self, edges, color="black") -> None:
        
        for i in range(len(edges)-1):
            self.graph.add_edges(edges[i], edges[i+1], color)
    
    # for preventing coordinate to be None.
    def checkPos(self, coordinate) -> int:
        
        return coordinate or 0
    
    def addPos(self, pos) -> None:
        
        nodes = self.graph.nodes()
        for node in nodes:
            self.graph.add_node(node, pos=pos[node])
    
    def addNode(self, node, x=None, y=None) -> None:
        
        # if x or y is initialized position will be added with the node.
        if x or y:
            self.graph.add_node(node, checkPos(x), checkPos(y))
        else:
            self.graph.add_node(node)
                
    def addNodes(self, nodes, pos={}) -> None:
        
        if pos:
            self.graph.add_nodes_from(nodes, pos)
        else:
            self.graph.add_nodes_from(nodes)

    def saveImage(self):
        
        pass
    
    def closeWindow(self):
        
        cv2.destroyAllWindows()
