def dfs(graph, start, visited):
    visited[start] = True
    res1.append(start)

    for i in graph[start]:
        if not visited[i]:
            visited[start] = True
            dfs(graph, i, visited)

#from collections import deque
def bfs(graph, start, visited):
    queue = [start]
    visited[start] = True

    while queue:
        node = queue.pop(0)
        res2.append(node)

        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, s = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for g in graph:
    g.sort()

res1 = []
res2 = []
visited = [False] * (n+1)               
dfs(graph, s, visited)
visited = [False] * (n+1)    
bfs(graph, s, visited)
print(*res1)
print(*res2)
