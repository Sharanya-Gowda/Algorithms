from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)
    
    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

if __name__ == "__main__":
    g = Graph()
    n = int(input("Enter the number of edges: "))
    print("Enter edges in format 'u v' (space-separated):")
    for _ in range(n):
        u, v = map(int, input().split())
        g.add_edge(u, v)
    
    start_vertex = int(input("Enter the starting vertex for traversal: "))
    print("\nDepth-First Search (DFS) starting from vertex", start_vertex)
    g.dfs(start_vertex)
    
