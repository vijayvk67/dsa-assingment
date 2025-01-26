class Graph:
    def __init__(self):
        # Initialize an empty graph dictionary to store vertices and edges
        self.graph = {}

    def vertex(self, node):
        # Add a new vertex to the graph if it's not already present
        if node not in self.graph:
            self.graph[node] = []

    def edge(self, vertex1, vertex2):
        # Add an undirected edge between vertex1 and vertex2
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def display(self):
        # Display the graph in "vertex -> [adjacent vertices]" format
        for vertex in self.graph:
            print(f"{vertex} -> {', '.join(self.graph[vertex])}")

    def dls(self, start, goal, limit):
        # Perform Depth-Limited Search (DLS)
        stack = [(start, 0)]  # Stack holds (current vertex, current depth)
        visited = set()  # Set to track visited nodes

        while stack:
            current_vertex, current_depth = stack.pop()

            # If the goal is found, return the goal
            if current_vertex == goal:
                print(f"Goal {goal} found at depth {current_depth}")
                return

            # If depth limit is reached, stop exploring further
            if current_depth >= limit:
                continue

            # Mark the node as visited and explore its neighbors
            visited.add(current_vertex)

            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    stack.append((neighbor, current_depth + 1))

        print(f"Goal {goal} not found within depth limit {limit}.")

# Example Usage

# Create a graph
g = Graph()

# Add vertices to the graph
g.vertex('a')
g.vertex('b')
g.vertex('c')
g.vertex('d')
g.vertex('e')
g.vertex('f')

# Add edges (undirected graph)
g.edge('a', 'b')
g.edge('a', 'c')
g.edge('b', 'e')
g.edge('b', 'd')
g.edge('c', 'e')
g.edge('c', 'f')

# Display the graph
g.display()

# Perform Depth-Limited Search
g.dls('a', 'b', 4)  # Search for 'e' from 'a' with a depth limit of 2
g.dls('a', 'f', 2)  # Search for 'f' from 'a' with a depth limit of 2
g.dls('a', 'f', 3)  # Search for 'f' from 'a' with a depth limit of 3
