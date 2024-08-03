def prim(graph, start_vertex):
    mst = []
    edges = []
    visited = set()

    def add_edges(vertex):
        visited.add(vertex)
        for neighbor, weight in graph[vertex]:
            if neighbor not in visited:
                edges.append((weight, vertex, neighbor))

    add_edges(start_vertex)

    while edges:
        edges.sort()
        weight, u, v = edges.pop(0)
        if v not in visited:
            mst.append((u, v, weight))
            add_edges(v)
    return mst

def get_user_input():
    graph = {}
    num_vertices = int(input("Enter the number of vertices: "))
    for _ in range(num_vertices):
        vertex = input("Enter vertex: ")
        graph[vertex] = []
        num_edges = int(input(f"Enter the number of edges for vertex {vertex}: "))
        for _ in range(num_edges):
            neighbor = input("Enter neighbor vertex: ")
            weight = int(input(f"Enter weight for edge {vertex}-{neighbor}: "))
            graph[vertex].append((neighbor, weight))
    start_vertex = input("Enter the start vertex: ")
    return graph, start_vertex

graph, start_vertex = get_user_input()
mst = prim(graph, start_vertex)
print("Minimum spanning tree:", mst)
