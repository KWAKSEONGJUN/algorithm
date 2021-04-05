n = int(input())

schedule = [[0]*2 for i in range(n)]
for i in range(n):
    schedule[i][1], schedule[i][0] = map(int, input().split())
    
schedule.sort(key=lambda x:(x[0], x[1]))

fe, res = 0, 0
for e, s in schedule:
    if s >= fe:
        res += 1
        fe = e

print(res)



