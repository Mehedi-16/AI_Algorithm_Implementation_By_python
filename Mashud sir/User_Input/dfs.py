# Input Format:
# 10             # ➤ Total number of edges
# 5 3            # ➤ Edge: 5 → 3
# 5 7            # ➤ Edge: 5 → 7
# 3 2            # ➤ Edge: 3 → 2
# 3 4            # ➤ Edge: 3 → 4
# 7 8            # ➤ Edge: 7 → 8
# 2 9            # ➤ Edge: 2 → 9
# 4 8            # ➤ Edge: 4 → 8
# 4 10           # ➤ Edge: 4 → 10
# 8 11           # ➤ Edge: 8 → 11
# 8 12           # ➤ Edge: 8 → 12
# 5              # ➤ Start node for DFS traversal

# ✅ DFS Code:


from collections import defaultdict

graph = defaultdict(list)
visited = set()

e = int(input())  # ➤ Number of edges
for _ in range(e):
    u, v = input().split()
    graph[u].append(v)

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

start = input()  # ➤ Start node
print("\n🔍 DFS Traversal Output:")
dfs(visited, graph, start)
