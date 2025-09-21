import heapq
from collections import defaultdict

graph = defaultdict(list)
heuristic = {}

e = int(input())  # Number of edges
for _ in range(e):
    u, v = input().split()
    graph[u].append(v)

nodes = input().split()  # List of all nodes
for node in nodes:
    heuristic[node] = int(input())  # Heuristic value for each node

def greedy_best_first_search(graph, start, goal, heuristic):
    visited = set()
    queue = [(heuristic[start], start, [start])]

    while queue:
        priority, current_node, current_path = heapq.heappop(queue)

        if current_node == goal:
            return current_path

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(queue, (heuristic[neighbor], neighbor, current_path + [neighbor]))

    return None

start = input("Start node: ")
goal = input("Goal node: ")

result = greedy_best_first_search(graph, start, goal, heuristic)
print("Greedy Best-First Search Path:", result)