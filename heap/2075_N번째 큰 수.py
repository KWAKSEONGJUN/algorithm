import sys
import heapq
input = sys.stdin.readline

n = int(input())
table = list(map(int, input().split()))
queue = table
heapq.heapify(queue)

for _ in range(n-1):
    table = list(map(int, input().split()))
    for v in table:
        if queue[0] < v:
            heapq.heappush(queue, v)
            heapq.heappop(queue)

print(queue[0])

