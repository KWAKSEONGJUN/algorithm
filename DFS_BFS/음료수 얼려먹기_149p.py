n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    
    if graph[i][j] == 0:
        graph[i][j] = 1

        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
        return True
    return False

res = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            res += 1

print(res)

