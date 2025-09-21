import heapq

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    queue = [(heuristic[start], start, [start])]

    while queue:
        h, node, path = heapq.heappop(queue)
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (heuristic[neighbor], neighbor, path + [neighbor]))
    return None

graph = {}
heuristic = {}

e = int(input())
for _ in range(e):
    u, v = input().split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, [])

for node in graph:
    heuristic[node] = int(input())

start = input()
goal = input()

path = best_first_search(graph, start, goal, heuristic)

if path:
    print(" → ".join(path))
else:
    print("No path found.")
