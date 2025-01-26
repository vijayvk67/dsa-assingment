import heapq
def ucs(graph,start,goal):
    pq=[]
    heapq.heappush(pq,(0,start))
    costs={node:float('inf')for node in graph}
    costs[start]=0
    parent={}
    parent[start]=None
    visited=set()
    while pq:
        current_cost,current_node=heapq.heappop(pq)
        if current_node==goal:
            return construct_path(parent,goal)
        if current_node in visited:
            continue#we using if visited we move for next node  if not visitded it will shift
        visited.add(current_node)
        for neighbour,cost in graph[current_node].items():
            new_cost=costs[current_node]+cost# neighbour costs is infinity at the start
            if new_cost<costs[neighbour]:
                costs[neighbour]=new_cost
                parent[neighbour]=current_node
                heapq.heappush(pq,(new_cost,neighbour))
    return "nopath"
def construct_path(parent,goal):
            path=[]
            current_node=goal
            while current_node is not None:
                path.append(current_node)
                current_node=parent.get(current_node)
            return list(reversed(path))
                
                
                
graph = {  
    'A': {'B': 1, 'C': 4},  
    'B': {'D': 3, 'E': 7},  
    'C': {'F': 2},  
    'D': {'F': 5},  
    'E': {'F': 2},  
    'F': {}  
}  

start = 'A'  
goal = 'f'  
path = ucs(graph,start,goal)

if path != "nopath":  
    print("Shortest Path:", "->".join(path))  
else:  
    print("No path found")
                
            
        
        
    