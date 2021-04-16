from copy import deepcopy
from collections import deque

total = 0
answer = -1
n, m = map(int, input().split())
graph = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
         
point = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            point.append((i, j))

def bfs(graph, visited, point):
    global n, m
    global total

    total += 1
    queue = deque()
    for i, j in point:
        queue.append([i, j])
        visited[i][j] = True

        while queue:
            u, v = queue.popleft()
            graph[u][v] = 2

            if u-1 >=0 and not visited[u-1][v] and graph[u-1][v] == 0:
                visited[u-1][v] = True
                queue.append([u-1, v])
            if u+1 < n and not visited[u+1][v] and graph[u+1][v] == 0:
                visited[u+1][v] = True
                queue.append([u+1, v])
            if v-1 >=0 and not visited[u][v-1] and graph[u][v-1] == 0:
                visited[u][v-1] = True
                queue.append([u, v-1])
            if v+1 < m and not visited[u][v+1] and graph[u][v+1] == 0:
                visited[u][v+1] = True
                queue.append([u, v+1])
        

def a(pos, visited, wall, graph):
    global answer
    global n, m
    global point

    if pos == 3:
        tmp = deepcopy(graph)
        for i, j in wall:
            tmp[i][j] = 1

        tmp_visited = [[False] * m for _ in range(n)]
        
        bfs(tmp, tmp_visited, point)

        cnt = 0
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 0:
                    cnt += 1
        answer = max(answer, cnt)
        return
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 0:
                visited[i][j] = True
                wall.append([i, j])
                a(pos+1, visited, wall, graph)
                wall.pop()
                visited[i][j] = False



visited = [[False] * m for _ in range(n)]
wall = []
a(0, visited, wall, graph)
print(answer)
print(total)
