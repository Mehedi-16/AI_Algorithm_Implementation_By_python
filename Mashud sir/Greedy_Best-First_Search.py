import heapq

graph = {
    'A': ['B', 'E'],
    'B': ['C', 'G'],
    'E': ['D'],
    'D': ['G'],
    'C': [],
    'G': []
}

heuristic = {
    'A': 11,
    'B': 6,
    'C': 99,
    'D': 1,
    'E': 7,
    'G': 0
}

def gbfs(graph, start, goal, heuristic):
    visited = set()
    queue = [(heuristic[start], start, [start])]

    while queue:
        _, node, path = heapq.heappop(queue)
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (heuristic[neighbor], neighbor, path + [neighbor]))

gbfs(graph, 'A', 'G')
