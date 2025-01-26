class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.add_vertex(node)
        if neighbor not in self.graph:
            self.add_vertex(neighbor)
        self.graph[node].append(neighbor)
    
    def display(self):
        for vertex in self.graph:
            print(vertex + " -> " + str(self.graph[vertex]))

    def bfs(self, start):
        queue = [start]
        visited = set()
        
        while queue:
            curr = queue.pop(0)
            print(curr)

            for neighbor in self.graph[curr]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
    
    def dfs(self, start):
        visited = {start:True}
        stack=[start]
        while stack:
            curr=stack.pop()
            print(curr)
            for neighbour in self.graph[curr]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    visited[neighbour]=True
     

# Example usage
g = Graph()
g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_edge('a', 'b')
g.add_edge('a', 'c')
g.add_edge('c', 'b')
g.add_edge('b', 'd')
g.display()
print("\nBreadth-First Search starting from node 'a':")
g.bfs('a')
print("\nDepth-First Search starting from node 'a':")
g.dfs('a')
