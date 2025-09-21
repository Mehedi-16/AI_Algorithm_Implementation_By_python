graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

visited = []

def dfs(visited, graph, node, goal):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        if node == goal:
            print("\nGoal Node " + goal + " Found\n")
            return
        for neighbor in graph.get(node, []):
            dfs(visited, graph, neighbor, goal)

# Run DFS
dfs(visited, graph, 'A', 'E')
