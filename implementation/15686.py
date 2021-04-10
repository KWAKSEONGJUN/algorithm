from itertools import combinations

n, m = map(int, input().split())

city = []
for i in range(n):
    city.append(list(map(int, input().split())))

houses_pos = []
chickens_pos = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses_pos.append([i+1, j+1])

        if city[i][j] == 2:
            chickens_pos.append([i+1, j+1])

chickens_combin_list = list(combinations(chickens_pos, m))

res = 10000
for chickens_list in chickens_combin_list:
    mn_sum = 0
    for h in houses_pos:
        mn = 10000
        for c in chickens_list:
            distance = sum([abs(h[i] - c[i]) for i in range(2)])
            mn = min(mn, distance)
        mn_sum += mn
    res = min(mn_sum, res)

print(res)






