from collections import defaultdict

graph = defaultdict(list)
visited = set()

e = int(input())  # edge সংখ্যা
for _ in range(e):
    u, v = input().split()
    graph[u].append(v)

def dls(graph, node, depth_limit, current_depth=0):
    if current_depth > depth_limit or node in visited:
        return
    print(node)
    visited.add(node)
    for neighbour in graph[node]:
        dls(graph, neighbour, depth_limit, current_depth + 1)

start = input()  # শুরু নোড
limit = int(input())  # depth limit
print(f"\n🔍 Depth-Limited Search up to depth {limit}:")
dls(graph, start, limit)
