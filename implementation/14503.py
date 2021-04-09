n, m = map(int, input().split())
y, x, d = map(int, input().split())

map_ = []

for i in range(n):
    map_.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

map_[y][x] = 1
cnt = 1
rotate = 0
while True:
    if rotate == 4:
        d = (d + 1) % 4
        nd = (d + 2) % 4
        ny = y + dy[nd]
        nx = x + dy[nd]

        if 0 < nx < m-1 and 0 < ny < n-1 and map_[ny][nx] == 2:
            x, y, rotate = nx, ny, 0
        else:
            break
            
    d = (d + 3) % 4
    rotate += 1
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 < nx < m-1 and 0 < ny < n-1 and map_[ny][nx] == 0:
        cnt += 1
        map_[ny][nx] = 2
        x, y, rotate = nx, ny, 0

    print(y, x, d)
  
print(cnt)




    