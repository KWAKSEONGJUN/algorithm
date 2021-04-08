x, y = list(input())
y = int(y)

horiz = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8}

dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

res = 0
for i in range(8):
    nx = horiz[x] + dx[i]
    ny = y + dy[i]

    if  0 < nx < 9 and 0 < ny < 9:
        res += 1

print(res)

