class Graph:
    def __init__(self, nofver):
        self.nofver = nofver
        self.adjmat = [[0] * nofver for _ in range(nofver)]

    def add_edge(self, u, v, w):
        self.adjmat[u][v] = w
    def print(self):
        for row in self.adjmat:
            print(' '.join(map(str, row)))


# Get the number of vertices from user input
nofver = int(input("Enter the number of vertices: "))

# Initialize the graph with the given number of vertices
g = Graph(nofver)

# Example to add edges
# You can modify this part to add edges based on user input or predefined edges
edges = [
    (0, 1, 5),  # Example edge from vertex 0 to vertex 1 with weight 5
    (0, 2, 3),
    (1, 2, 2),
    (2, 3, 7),
    (3, 0, 4)
]

# Add edges to the graph
for u, v, w in edges:
    g.add_edge(u, v, w)

g.print()
