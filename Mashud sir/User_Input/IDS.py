def depth_limited_search(graph, node, goal, depth):
    if depth < 0:
        return None
    if node == goal:
        return [node]
    for neighbor in graph.get(node, []):
        path = depth_limited_search(graph, neighbor, goal, depth - 1)
        if path:
            return [node] + path
    return None

def iterative_deepening_search(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"🔍 Searching at depth {depth}...")
        path = depth_limited_search(graph, start, goal, depth)
        if path:
            return path
    return None

#Example graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

# 🚀 Start and goal nodes
start_node = 'A'
goal_node = 'H'
max_depth = 5

result = iterative_deepening_search(graph, start_node, goal_node, max_depth)
print("iterative_deepening_search:", result)
