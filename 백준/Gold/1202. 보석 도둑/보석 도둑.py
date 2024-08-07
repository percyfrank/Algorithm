import heapq
import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    jewels = [tuple(map(int, input().split())) for _ in range(n)]
    jewels = deque(sorted(jewels))
    bags = [int(input()) for _ in range(k)]
    bags.sort()

    answer = 0
    tmp = []
    for bag in bags:
        while jewels and bag >= jewels[0][0]:
            m, v = jewels.popleft()
            heapq.heappush(tmp, -v)
        if tmp:
            answer -= heapq.heappop(tmp)

    print(answer)