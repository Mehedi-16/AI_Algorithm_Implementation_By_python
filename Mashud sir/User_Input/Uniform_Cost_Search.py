import heapq
from collections import defaultdict

graph = defaultdict(list)


e = int(input())
for _ in range(e):
    u, v, c = input().split()
    c = int(c)
    graph[u].append((v, c))
    graph[v].append((u, c)) #🔁 Bi-directional edge added



def uniform_cost_search(graph, start, goal):
    visited = set()
    queue = [(0, start, [start])]

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node == goal:
            return path

        if node in visited:
            continue
        visited.add(node)

        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (cost + edge_cost, neighbor, path + [neighbor]))

    return None


start = input()
goal = input()

path = uniform_cost_search(graph, start, goal)
print("Greedy Best-First Search Path:", path)
