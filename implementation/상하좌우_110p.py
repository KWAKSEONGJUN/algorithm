n = int(input())
move = input().split()

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
move_types = ['R', 'L', 'U', 'D']

for m in move:
    i = move_types.index(m)
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    else:
        x, y = nx, ny

print(x, y)

