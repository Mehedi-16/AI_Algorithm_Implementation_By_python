import heapq
graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'E': [('D', 6)],
    'D': [('G', 1)]
}

heuristic = {
    'A': 11,
    'B': 6,
    'C': 99,
    'D': 1,
    'E': 7,
    'G': 0
}

def a_star(graph, start, goal, heuristic):
     visited = set()
     queue = [(heuristic[start], 0, start, [start])]  # (f, g, node, path)
   

     while queue:
        f, g, node, path = heapq.heappop(queue)

        if node == goal:
            return g, path 

        if node in visited:
            continue
        visited.add(node)

        for neighbor, cost in graph.get(node, []):
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(queue, (new_f, new_g, neighbor, path + [neighbor]))

     return float("inf"), []  # Goal not reachable



cost, path = a_star(graph, 'A', 'G', heuristic)
print("A* Search Path:",path)
print("Total Cost:", cost)
