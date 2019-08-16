def dijkstra(graph, source, destination, predecessor={}, distances={}, visited=[]):
    
    """
    SOURCE:
    http://www.gilles-bertrand.com/2014/03/dijkstra-algorithm-python-example-source-code-shortest-path.html
    
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
        
        # next recursion will use the lowest cost neighbor as new source.
        new_source = min(unvisited, key=unvisited.get)
        return dijkstra(graph, new_source, destination, predecessor, distances, visited)

def europeMap(source, destination):
    graph = {'Edinburgh': {'London': 4}, 'London': {'Edinburgh': 4, 'Dieppe': 2, 'Amsterdam': 2}, 'Dieppe': {'London': 2, 'Brest': 2, 'Paris': 1, 'Bruxelles': 2}, 'Brest': {'Dieppe': 2, 'Pamplona': 4, 'Paris': 3}, 'Pamplona': {'Brest': 4, 'Madrid': 3, 'Barcelona': 2, 'Marseille': 4, 'Paris': 4}, 'Paris': {'Brest': 3, 'Dieppe': 1, 'Pamplona': 4, 'Marseille': 4, 'Bruxelles': 2, 'Zurich': 3, 'Frankfurt': 3}, 'Bruxelles': {'Dieppe': 2, 'Amsterdam': 1, 'Paris': 2, 'Frankfurt': 2}, 'Amsterdam': {'London': 2, 'Bruxelles': 1, 'Essen': 3, 'Frankfurt': 2}, 'Madrid': {'Pamplona': 3, 'Lisboa': 3, 'Cadiz': 3, 'Barcelona': 2}, 'Lisboa': {'Madrid': 3, 'Cadiz': 2}, 'Cadiz': {'Lisboa': 2, 'Madrid': 3}, 'Barcelona': {'Madrid': 2, 'Pamplona': 2, 'Marseille': 4}, 'Marseille': {'Barcelona': 4, 'Pamplona': 4, 'Paris': 4, 'Zurich': 2, 'Roma': 4}, 'Zurich': {'Paris': 3, 'Marseille': 2, 'Munchen': 2, 'Venezia': 2}, 'Frankfurt': {'Paris': 3, 'Amsterdam': 2, 'Bruxelles': 2, 'Munchen': 2, 'Essen': 2, 'Berlin': 3}, 'Essen': {'Amsterdam': 3, 'Kobenhavn': 3, 'Berlin': 2, 'Frankfurt': 2}, 'Munchen': {'Frankfurt': 2, 'Zurich': 2, 'Venezia': 2, 'Wien': 3}, 'Venezia': {'Zurich': 2, 'Roma': 2, 'Munchen': 2, 'Zagrab': 2}, 'Roma': {'Marseille': 4, 'Venezia': 2, 'Palermo': 4, 'Brindisi': 2}, 'Palermo': {'Roma': 4, 'Brindisi': 3, 'Smyrna': 6}, 'Brindisi': {'Roma': 2, 'Palermo': 3, 'Athina': 4}, 'Kobenhavn': {'Essen': 3, 'Stockholm': 3}, 'Berlin': {'Essen': 2, 'Frankfurt': 3, 'Danzig': 4, 'Warzawa': 4, 'Wien': 3}, 'Stockholm': {'Kobenhavn': 3, 'Petrograd': 8}, 'Petrograd': {'Stockholm': 8, 'Riga': 4, 'Wilno': 4, 'Moskva': 4}, 'Danzig': {'Berlin': 4, 'Riga': 3, 'Warzawa': 2}, 'Warzawa': {'Berlin': 4, 'Wien': 4, 'Danzig': 2, 'Wilno': 3, 'Kyiv': 4}, 'Wien': {'Berlin': 3, 'Munchen': 3, 'Zagrab': 2, 'Warzawa': 4, 'Budapest': 1}, 'Zagrab': {'Venezia': 2, 'Wien': 2, 'Budapest': 2, 'Sarajevo': 3}, 'Budapest': {'Wien': 1, 'Zagrab': 2, 'Sarajevo': 3, 'Bucuresti': 4, 'Kyiv': 6}, 'Riga': {'Danzig': 3, 'Petrograd': 4, 'Wilno': 4}, 'Wilno': {'Riga': 4, 'Warzawa': 3, 'Petrograd': 4, 'Smolensk': 3, 'Kyiv': 2}, 'Moskva': {'Petrograd': 4, 'Smolensk': 2, 'Kharkov': 4}, 'Smolensk': {'Wilno': 3, 'Moskva': 2, 'Kyiv': 3}, 'Kyiv': {'Wilno': 2, 'Budapest': 6, 'Warzawa': 4, 'Smolensk': 3, 'Bucuresti': 4, 'Kharkov': 4}, 'Smyrna': {'Palermo': 6, 'Athina': 2, 'Constantinople': 2, 'Angora': 3}, 'Athina': {'Brindisi': 4, 'Sarajevo': 4, 'Sofia': 3, 'Smyrna': 2}, 'Sarajevo': {'Zagrab': 3, 'Athina': 4, 'Budapest': 3, 'Sofia': 2}, 'Sofia': {'Sarajevo': 2, 'Athina': 3, 'Bucuresti': 2, 'Constantinople': 3}, 'Bucuresti': {'Budapest': 4, 'Sofia': 2, 'Kyiv': 4, 'Constantinople': 3, 'Sevastapol': 4}, 'Constantinople': {'Sofia': 3, 'Bucuresti': 3, 'Smyrna': 2, 'Sevastapol': 4, 'Angora': 2}, 'Sevastapol': {'Bucuresti': 4, 'Constantinople': 4, 'Rostov': 4, 'Sochi': 2, 'Erzurum': 4}, 'Kharkov': {'Kyiv': 4, 'Moskva': 4, 'Rostov': 2}, 'Rostov': {'Kharkov': 2, 'Sevastapol': 4, 'Sochi': 2}, 'Sochi': {'Sevastapol': 2, 'Rostov': 2, 'Erzurum': 3}, 'Erzurum': {'Sochi': 3, 'Sevastapol': 4, 'Angora': 3}, 'Angora': {'Erzurum': 3, 'Constantinople': 2, 'Smyrna': 3}}    
    return dijkstra(graph, source, destination)

if __name__ == '__main__':
    print(europeMap('Edinburgh', 'London'))