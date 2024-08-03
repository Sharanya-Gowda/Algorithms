class BellmanFord:
    MAX_VALUE = float('inf')

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.distances = [self.MAX_VALUE] * (num_vertices + 1)

    def evaluate(self, source, adj_matrix):
        self.distances[source] = 0

        for _ in range(1, self.num_vertices):
            for u in range(1, self.num_vertices + 1):
                for v in range(1, self.num_vertices + 1):
                    if adj_matrix[u][v] != self.MAX_VALUE:
                        if self.distances[v] > self.distances[u] + adj_matrix[u][v]:
                            self.distances[v] = self.distances[u] + adj_matrix[u][v]

        for u in range(1, self.num_vertices + 1):
            for v in range(1, self.num_vertices + 1):
                if adj_matrix[u][v] != self.MAX_VALUE:
                    if self.distances[v] > self.distances[u] + adj_matrix[u][v]:
                        print("The graph contains a negative edge cycle")
                        return

        for vertex in range(1, self.num_vertices + 1):
            print(f"Distance of source {source} to {vertex} is {self.distances[vertex]}")

def main():
    num_vertices = int(input("Enter the number of vertices: "))
    adj_matrix = [[0] * (num_vertices + 1) for _ in range(num_vertices + 1)]

    print("Enter the adjacency matrix:")
    for i in range(1, num_vertices + 1):
        for j in range(1, num_vertices + 1):
            adj_matrix[i][j] = int(input(f"Edge from {i} to {j}: "))
            if i == j:
                adj_matrix[i][j] = 0
            elif adj_matrix[i][j] == 0:
                adj_matrix[i][j] = BellmanFord.MAX_VALUE

    source = int(input("Enter the source vertex: "))
    bf = BellmanFord(num_vertices)
    bf.evaluate(source, adj_matrix)

if __name__ == "__main__":
    main()
