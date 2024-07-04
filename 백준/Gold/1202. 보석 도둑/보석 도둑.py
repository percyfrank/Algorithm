import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
jewels.sort()
bags.sort()

answer = 0
tmp = []
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(tmp, -jewels[0][1])
        heapq.heappop(jewels)

    if tmp:
        answer -= heapq.heappop(tmp)

print(answer)