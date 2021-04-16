def dfs(map_, i, j, visited):
    visited[i][j] = True

    cnt = 1
    if i - 1 >= 0 and not visited[i-1][j] and map_[i-1][j] == 1:
        cnt += dfs(map_, i-1, j, visited)

    if i + 1 < n and not visited[i+1][j] and map_[i+1][j] == 1:
        cnt += dfs(map_, i+1, j, visited)

    if j - 1 >= 0 and not visited[i][j-1] and map_[i][j-1] == 1:
        cnt += dfs(map_, i, j-1, visited)

    if j + 1 < n and not visited[i][j+1] and map_[i][j+1] == 1:
        cnt += dfs(map_, i, j+1, visited)

    return cnt


n = int(input())

map_ = []
for _ in range(n):
    tmp = list(map(int, input()))
    map_.append(tmp)

visited = [[False] * n for _ in range(n)]

cnt = 0
houses = []
for i in range(n):
    for j in range(n):
        if map_[i][j] == 1 and not visited[i][j]:
            houses.append(dfs(map_, i, j, visited))
            cnt += 1

houses.sort()
print(cnt)
for house in houses:
    print(house)