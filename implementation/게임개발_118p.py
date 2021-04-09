n, m = map(int, input().split())
y, x, d = map(int, input().split())

map_ = []

for i in range(n):
    map_.append(list(map(int, input().split())))
map_[0] = [0] * m
map_[n-1] = [0] * m

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

cnt = 0
rotate = 0
while True:
    d = (d + 3) % 4
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 < nx <= m and 0 < ny <= n and map_[ny-1][nx-1] == 1:
        x, y, rotate = nx, ny, 0
        cnt += 1
        map_[ny-1][nx-1] += 1
    else:
        rotate += 1
        if rotate == 4:
            nd = d + 2 % 4
            ny = y + dy[nd]

            if ny < 1 or ny > n or map_[ny-1][nx-1] == 0:
                break
    
print(cnt)




    