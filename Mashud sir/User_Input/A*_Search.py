import heapq
from collections import defaultdict
graph = defaultdict(list)
heuristic = {}

e = int(input())
for _ in range(e):
    u, v, c = input().split()
    c = int(c)
    graph[u].append((v, c))

nodes = input().split()  # List of all nodes
for node in nodes:
    heuristic[node] = int(input())  # Heuristic value for each node


def a_star_search(graph, start, goal, heuristic):
    queue = [(heuristic[start], 0, start, [start])]  # (f = g + h, g, node, path)
    visited = set()

    while queue:
        f, g, node, path = heapq.heappop(queue)

        if node == goal:
            return path

        if node in visited:
            continue
        visited.add(node)

        for neighbor, cost in graph.get(node, []):
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(queue, (new_f, new_g, neighbor, path + [neighbor]))

    return None


start = input()
goal = input()


path = a_star_search(graph, start, goal, heuristic)
print("A* Search Path:", path)