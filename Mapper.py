graph = {}
pos = {}

while True:
    
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
    
print(graph)