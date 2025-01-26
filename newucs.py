import heapq

def ucs(graph, start, goal):
    pq = []
    heapq.heappush(pq, (0, start))
    costs = {node: float('inf') for node in graph}
    costs[start] = 0
    parent = {}
    parent[start] = None
    visited = set()
    
    while pq:
        current_cost, current_node = heapq.heappop(pq)
        
        if current_node == goal:
            return construct_path(parent, goal)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        for neighbor, cost in graph[current_node].items():
            new_cost = costs[current_node] + cost
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parent[neighbor] = current_node
                heapq.heappush(pq, (new_cost, neighbor))
    
    return "No path found"

def construct_path(parent, goal):
    path = []
    current_node = goal
    
    while current_node is not None:
        path.append(current_node)
        current_node = parent.get(current_node)
    
    return list(reversed(path))

# Example usage:
graph = {  
    'A': {'B': 1, 'C': 4},  
    'B': {'D': 3, 'E': 7},  
    'C': {'F': 2},  
    'D': {'F': 5},  
    'E': {'F': 2},  
    'F': {}  
}  

start = 'A'  
goal = 'F'  
path = ucs(graph, start, goal)

if path != "No path found":  
    print("Shortest Path:", "->".join(path))  
else:  
    print("No path found")
