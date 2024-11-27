def bellman_ford(graph, vertices, start):
   
    distances = {vertex: float('inf') for vertex in vertices}
    distances[start] = 0
    
   
    for _ in range(len(vertices) - 1):
        for u, edges in graph.items():
            for v, weight in edges.items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    
    
    for u, edges in graph.items():
        for v, weight in edges.items():
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative weight cycle")
    
    return distances


##Example form TB
graph = {
    's': {'t': 6, 'y': 7},
    't': {'x': 5, 'y': 8, 'z': -4},
    'x': {'t': -2},
    'y': {'x': -3, 'z': 9},
    'z': {'s': 2, 'x': 7}
}
vertices = ['s', 't', 'x', 'y', 'z']


try:
    result = bellman_ford(graph, vertices, 's')
    print("Shortest distances from 's':")
    for vertex, distance in result.items():
        print(f"{vertex}: {distance}")
except ValueError as e:
    print(e)



