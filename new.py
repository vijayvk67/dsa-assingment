class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex): 
         # we are usinf the if condition becas if there  is a repeated vertex thn it wont print  or add vertex in the graphit will print the else part 
        if vertex not in self.graph:
            self.graph[vertex] = []
        else:
            print("the vertex present in the graph",vertex)

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)  # For undirected graph
    def display(self):
        for vertex in self.graph:
           print(vertex + " -> " + str(self.graph[vertex]))



    def bfs(self,start_vertex):
        quee=[start_vertex]#we are implementing queue by using list by the logic we are adding all the vertex in the list
        #then we are crating a dictionary because the time complexity of the list is high so we are creating a dictionary
        visited={start_vertex:True}#we are checking i there a strt vertex in this visited we will add the vertex which is transversedwith the  through the graph

        while quee: #curr is quee. pop(0) because the list strts with the 0 index and if  the adjacent vertex are there in the queue it wil pop

            curr=quee.pop(0)
            print(curr)

            for neig in self.graph[curr]:
                if  neig not in visited:
                    quee.append(neig)#if the 
                    visited[neig]=True



    
    def dfs(self, start_vertex):
       stack = [start_vertex]  # Stack initialization with the start vertex
       visited = {start_vertex: True}  # Dictionary to keep track of visited nodes it stroing the vertex as key and and value set to true 

       while stack:
        curr = stack.pop()  
        print(curr)

        for neighbor in self.graph[curr]:
            if neighbor not in visited:
                stack.append(neighbor)  # Add the unvisited neighbor to the stack
                visited[neighbor] = True                 

# Example usage
g = Graph() 
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('E', 'F')

g.display()
print("the given vertices to df tree is",g.bfs('A')) 

g.dfs( 'A')
