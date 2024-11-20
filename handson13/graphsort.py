
from typing import List, Dict, Set, Tuple
from collections import defaultdict

class Graph:
    def __init__(self):
       
        self.graph = defaultdict(list)
        self.vertices = set()
    
    def add_edge(self, u, v):
        
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph[u].append(v)
    
    def is_cyclic_util(self, v: str, visited: Dict[str, bool], 
                       rec_stack: Dict[str, bool]) -> bool:
        
        # Mark current node as visited and add to recursion stack
        visited[v] = True
        rec_stack[v] = True
        
        # Recur for all neighbors
        for neighbor in self.graph[v]:
            # If vertex is not visited, then explore it
            if not visited.get(neighbor, False):
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            
            # If neighbor is in recursion stack, a cycle is detected
            elif rec_stack.get(neighbor, False):
                return True
        
        # Remove vertex from recursion stack
        rec_stack[v] = False
        return False
    
    def is_cyclic(self) -> bool:
        
        # Mark all vertices as not visited
        visited = {v: False for v in self.vertices}
        rec_stack = {v: False for v in self.vertices}
        
        # Check for cycle in DFS traversal
        for vertex in self.vertices:
            if not visited[vertex]:
                if self.is_cyclic_util(vertex, visited, rec_stack):
                    return True
        
        return False
    
    def topological_sort(self) -> List:
       
        # Check for cycles before topological sort
        if self.is_cyclic():
            raise ValueError("Topological sort is not possible for a cyclic graph")
        
        # Track visited vertices and result stack
        visited = {v: False for v in self.vertices}
        stack = []
        
        def dfs(v):
            # Mark current node as visited
            visited[v] = True
            
            # Recur for all adjacent vertices
            for neighbor in self.graph[v]:
                if not visited.get(neighbor, False):
                    dfs(neighbor)
            
            # Push current vertex to stack
            stack.append(v)
        
        # Call DFS for all unvisited vertices
        for v in self.vertices:
            if not visited[v]:
                dfs(v)
        
        # Return reversed stack (topological order)
        return stack[::-1]
    
    def depth_first_search(self, start) -> List:
        
        visited = {v: False for v in self.vertices}
        path = []
        
        def dfs(v):
            # Mark current node as visited
            visited[v] = True
            path.append(v)
            
            # Recur for all adjacent vertices
            for neighbor in self.graph[v]:
                if not visited.get(neighbor, False):
                    dfs(neighbor)
        
        # Start DFS from the given vertex
        if start not in self.vertices:
            raise ValueError(f"Starting vertex {start} not in graph")
        
        dfs(start)
        return path

class KruskalGraph:
    def __init__(self):
        
        self.graph = []
        self.vertices = set()
    
    def add_edge(self, u, v, weight):
        
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph.append((u, v, weight))
    
    def find(self, parent: Dict, i):
        
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]
    
    def union(self, parent: Dict, rank: Dict, x, y):
        
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        
        # Attach smaller rank tree under root of high rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    
    def kruskal_mst(self) -> List[Tuple]:
    
        # Result to store MST
        result = []
        
        # Sort edges by weight
        self.graph = sorted(self.graph, key=lambda item: item[2])
        
        # Create parent and rank dictionaries
        parent = {v: v for v in self.vertices}
        rank = {v: 0 for v in self.vertices}
        
        # Process edges
        for edge in self.graph:
            u, v, w = edge
            x = self.find(parent, u)
            y = self.find(parent, v)
            
            # If including this edge doesn't create a cycle, add it
            if x != y:
                result.append((u, v, w))
                self.union(parent, rank, x, y)
        
        return result

def interactive_graph_input(graph_type):

    if graph_type == 'topological' or graph_type == 'dfs':
        graph = Graph()
        print("\nEnter Directed Graph Edges (type 'done' when finished):")
        print("Format: source destination")
    elif graph_type == 'kruskal':
        graph = KruskalGraph()
        print("\nEnter Weighted Graph Edges (type 'done' when finished):")
        print("Format: source destination weight")
    else:
        raise ValueError("Invalid graph type")
    
    while True:
        try:
            # Prompt for edge input
            if graph_type == 'kruskal':
                edge_input = input("Enter weighted edge (src dest weight): ").strip()
            else:
                edge_input = input("Enter directed edge (src dest): ").strip()
            
            # Check for termination
            if edge_input.lower() == 'done':
                break
            
            # Parse input
            parts = edge_input.split()
            
            if graph_type == 'kruskal':
                if len(parts) != 3:
                    print("Invalid input. Enter source, destination, and weight.")
                    continue
                u, v, weight = parts[0], parts[1], int(parts[2])
                graph.add_edge(u, v, weight)
            else:
                if len(parts) != 2:
                    print("Invalid input. Enter source and destination.")
                    continue
                u, v = parts[0], parts[1]
                graph.add_edge(u, v)
        
        except ValueError as e:
            print(f"Error: {e}")
            continue
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            continue
    
    return graph

def main():
    while True:
        print("\n--- Graph Algorithms ---")
        print("1. Check if Graph is Cyclic")
        print("2. Topological Sort")
        print("3. Depth-First Search")
        print("4. Kruskal's Minimum Spanning Tree")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        try:
            if choice == '1':
                graph = interactive_graph_input('dfs')
                is_cyclic = graph.is_cyclic()
                print("\nGraph is " + ("Cyclic" if is_cyclic else "Acyclic"))
            
            elif choice == '2':
                graph = interactive_graph_input('topological')
                try:
                    result = graph.topological_sort()
                    print("\nTopological Sort Result:", result)
                except ValueError as e:
                    print(f"\nError: {e}")
                    print("Hint: A cyclic graph prevents topological sorting")
                    print("Example of a cyclic graph: A -> B -> C -> A")
            
            elif choice == '3':
                graph = interactive_graph_input('dfs')
                start = input("Enter starting vertex: ").strip()
                try:
                    result = graph.depth_first_search(start)
                    print("\nDFS Result:", result)
                except ValueError as e:
                    print(f"\nError: {e}")
            
            elif choice == '4':
                graph = interactive_graph_input('kruskal')
                result = graph.kruskal_mst()
                print("\nMinimum Spanning Tree Edges:")
                for edge in result:
                    print(f"{edge[0]} -- {edge[1]} : {edge[2]}")
            
            elif choice == '5':
                print("Exiting...")
                break
            
            else:
                print("Invalid choice. Please try again.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()