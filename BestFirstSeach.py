#Best First Search Algorithm
from queue import PriorityQueue

def best_first_search(start, goal, graph, heuristic):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start, None))  # add None as parent of start node
    
    parents = {}
    
    while not queue.empty():
        cost, node, parent = queue.get()
        parents[node] = parent
        
        if node == goal:
            path = []
            current = node
            while current != start:
                path.append(current)
                current = parents[current]
            path.append(start)
            path.reverse()
            return path
        
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                priority = heuristic[neighbor]
                queue.put((priority, neighbor, node))  # add current node as parent of neighbor
    
    return None
# Sample graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Sample heuristic function
heuristic = {
    'A': 10,
    'B': 8,
    'C': 7,
    'D': 6,
    'E': 4,
    'F': 0
}

# Call the function
start_node = 'A'
goal_node = 'F'
path = best_first_search(start_node, goal_node, graph, heuristic)

# Print the path
if path:
    print(f"Path from '{start_node}' to '{goal_node}': {' -> '.join(path)}")
else:
    print(f"Goal node '{goal_node}'not found!")