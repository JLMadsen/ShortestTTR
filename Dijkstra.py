def dijkstra(graph, source, destination, current_path, distances, visited):
    
    if source == destination:
        path = current_path
        weight = 0
        
        return path, weight
    
    
    return dijkstra(graph, source, destination, current_path, distances, visited)