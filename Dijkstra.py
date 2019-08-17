# for example shown beneath
from Board import Board
board = Board()

# you only need to give the first three parameters.
def dijkstra(graph, source, destination, predecessor={}, distances={}, visited=[]):
    
    """
    SOURCE:
    http://www.gilles-bertrand.com/2014/03/dijkstra-algorithm-python-example-source-code-shortest-path.html
    http://www.gilles-bertrand.com/2014/03/disjkstra-algorithm-description-shortest-path-pseudo-code-data-structure-example-image.html
    
    Modified to fit my program.
    
    graph format:
        {'node1': {'node2' : 4, 'node3' : 2}, 'node2': {'node1' : 4}, ...}
    Predecessor:
        "Structure that will keep for every node its father"
    """
    
    # Check if path is not possible
    if source not in graph or destination not in graph:
        #print(source, destination, graph)
        exit("No path availible")
    
    # Ending condition
    if source == destination:
        path = []
        pred = destination
        while pred != None:
            path.append(pred)
            # .get(pred,None) returns pred value if it exists, if not returns None
            pred=predecessor.get(pred,None)
        return path, distances[destination]
    else:
        # initialize cost
        if not visited:
            distances[source] = 0
        # visit neighbor
        for neighbor in graph[source]:
            
            if neighbor not in visited:
                
                new_distance = distances[source] + graph[source][neighbor]
                # if neighbor distance doesnt exit return infinite
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessor[neighbor] = source
        
        # add node to visited
        visited.append(source)
        
        # map all unvisited nodes
        unvisited = {}
        for node in graph:
            if node not in visited:
                unvisited[node] = distances.get(node,float('inf'))
        
        # for debugging, this list is empty sometimes when it shouldnt be
        if not unvisited:
            exit("no more unvisited nodes")
        
        # next recursion will use the lowest cost neighbor as new source.
        new_source = min(unvisited, key=unvisited.get)
        return dijkstra(graph, new_source, destination, predecessor, distances, visited)

# if you run this file it will just run an example
if __name__ == '__main__':
    print(dijkstra(board.getMap("Europe"), 'Edinburgh', 'Sochi'))