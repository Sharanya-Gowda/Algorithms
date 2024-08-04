#time complexity ElogV where E is edges and V is vertices
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

# Prompting user for graph input
print("Enter the graph in the format {'vertex': [('neighbor', weight), ...]}")
graph_input = input("Enter the graph: ")
graph = eval(graph_input)  # Using eval to parse the input as a dictionary

start_vertex = input("Enter the start vertex: ")

# Running Prim's algorithm
mst = prim(graph, start_vertex)
print("Minimum spanning tree:", mst)
