n = int(input())
arr = list(map(int, input().split()))

s = sum(arr)

res = 0
for i in arr:
  s -= i
  res += s * i

print(res)