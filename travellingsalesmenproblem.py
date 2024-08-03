from sys import maxsize 
from itertools import permutations

# Function to compute the minimum weight Hamiltonian Cycle using TSP
def travellingSalesmanProblem(graph, s, V):
    # store all vertex apart from source vertex 
    vertex = [] 
    for i in range(V): 
        if i != s: 
            vertex.append(i) 

    # store minimum weight Hamiltonian Cycle 
    min_path = maxsize 
    next_permutation = permutations(vertex)
    for i in next_permutation:
        # store current Path weight(cost) 
        current_pathweight = 0
        # compute current path weight 
        k = s 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 
        # update minimum 
        min_path = min(min_path, current_pathweight) 
    return min_path 

# Driver Code 
if _name_ == "_main_": 
    V = int(input("Enter the number of vertices: "))
    
    # Initialize graph as empty list
    graph = []
    
    # Take input for the adjacency matrix
    print("Enter the adjacency matrix (enter row-wise):")
    for i in range(V):
        row = list(map(int, input().split()))
        graph.append(row)
    
    s = 0  # Starting node (can be user-defined as well)
    print("Minimum cost:", travellingSalesmanProblem(graph,s,V))