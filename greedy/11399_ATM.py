n = int(input())
pi = list(map(int, input().split()))

pi = sorted(pi)

sum = 0
w = 0
for p in pi:
    sum = sum + w + p
    w += p

print(sum)