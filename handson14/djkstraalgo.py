import heapq

def dijkstra(graph, start):
    
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, curr_node = heapq.heappop(priority_queue)
        
        
        if current_distance > dist[curr_node]:
            continue
        
     
        for neighbor, weight in graph[curr_node].items():
            distance = current_distance + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return dist

# example form TB
graph = {
    's': {'t': 10, 'y': 5},
    't': {'x': 1, 'y': 2},
    'y': {'t': 3, 'x': 9, 'z': 2},
    'x': {'z': 4},
    'z': {'x': 6, 's': 7}
}

# Compute shortest paths from source 's'
result = dijkstra(graph, 's')

# Display results
print("Shortest dist from 's':")
for vertex, distance in result.items():
    print(f"{vertex}: {distance}")
