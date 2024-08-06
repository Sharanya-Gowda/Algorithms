def bellman(graph,src,v):
    dist=[float('inf')]*v
    dist[src]=0
    for i in range(v-1):
        for edge in graph:
            if(dist[edge[1]]>dist[edge[0]]+edge[2]):
                dist[edge[1]]=dist[edge[0]]+edge[2]
    for edge in graph:
        if(dist[edge[1]]>dist[edge[0]]+edge[2]):
            print("nrg cycle")
            return
    print("\nVertex\tDistance from source")
    for i in range(v):
        print(i,"\t",dist[i])

v=int(input("Enter num of vertices:"))
e=int(input("Enter the edges:"))
graph=[]
print("Enter adj list")
for i in range(e):
    graph.append(list(map(int,input().split())))
src=int(input("Enter source:"))
print(graph)
bellman(graph,src,v)
