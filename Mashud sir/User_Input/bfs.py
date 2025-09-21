from collections import defaultdict

graph = defaultdict(list)
visited = []
queue = []

e = int(input())  # edge সংখ্যা
for _ in range(e):
    u, v = input().split()
    graph[u].append(v)

def bfs(visited, graph, node, goal):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        if m == goal:
            print("\nGoal Node" + goal + " Found\n")
            return
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

start = input()  # শুরু নোড
goal = input()   # গন্তব্য নোড
bfs(visited, graph, start, goal)
