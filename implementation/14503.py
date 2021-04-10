n, m = map(int, input().split())
r, c, d = map(int, input().split())

map_ = []
for i in range(n):
    map_.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

cnt = 0
while True:
    if map_[r][c] == 0:
        map_[r][c] = 2
        cnt += 1

    flag = 0
    for i in range(4):
        d = (d + 3) % 4
        nr = r + dy[d]
        nc = c + dx[d]
   
        if map_[nr][nc] == 0:
            flag = 1
            r, c = nr, nc
            break;

    if flag == 0:
        nd = (d + 2) % 4
        nr = r + dy[nd]
        nc = c + dx[nd]

        if map_[nr][nc] == 1:
            break
        else:
            r, c = nr, nc

print(cnt)

        
    

        



