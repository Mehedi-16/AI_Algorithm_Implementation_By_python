import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    queue = [(heuristic[start], start, [start])]

    while queue:
        _, node, path = heapq.heappop(queue)

        if node == goal:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in path:
                heapq.heappush(queue, (heuristic[neighbor], neighbor, path + [neighbor]))

    return None


graph = {}
heuristic = {}

e = int(input())
for _ in range(e):
    u, v = input().split()
    if u not in graph:
        graph[u] = []
    graph[u].append(v)
    if v not in graph:
        graph[v] = []


print("\n Enter heuristic values for each node:")
for node in graph:
    h = int(input())
    heuristic[node] = h

start = input("\n🚀 Enter start node: ")
goal = input("🎯 Enter goal node: ")

path = greedy_best_first_search(graph, start, goal, heuristic)
print("Greedy Best-First Search Path:", path)
