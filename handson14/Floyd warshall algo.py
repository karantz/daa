def floyd_warshall(graph, vert):
    # Initialize the distance matrix
    dist = {u: {v: float('inf') for v in vert} for u in vert}
    
    # Set the distance to 0 for self-loops and initialize edges
    for u in vert:
        dist[u][u] = 0
    for u, edges in graph.items():
        for v, weight in edges.items():
            dist[u][v] = weight
    
    # Main algorithm: update dist using each vertex as an intermediate
    for k in vert:
        for i in vert:
            for j in vert:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist


# Define the new smaller graph
graph = {
    'P': {'Q': 3, 'R': 10},
    'Q': {'R': 1, 'S': 8},
    'R': {'S': 2},
    'S': {}
}
vert = ['P', 'Q', 'R', 'S']

# Run the Floyd-Warshall algorithm
result = floyd_warshall(graph, vert)

# Display the distance matrix
print("Shortest dist between all pairs:")
for u in vert:
    for v in vert:
        distance = result[u][v]
        if distance == float('inf'):
            print(f"{u} to {v}: ∞")
        else:
            print(f"{u} to {v}: {distance}")
