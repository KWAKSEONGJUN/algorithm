import sys
import heapq
input = sys.stdin.readline

n = int(input())

schedules = [tuple(map(int, input().split())) for _ in range(n)]
heap = [0]

for s, t in sorted(schedules):
    if heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap, t)

print(len(heap))

