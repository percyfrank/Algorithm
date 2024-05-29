
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split(" "))
target = list(map(int, input().split(" ")))
q = deque([i for i in range(1, n+1)])

cnt = 0
for pos in target:
    idx = q.index(pos)
    if idx <= len(q) / 2:
        while q[0] != pos:
            q.rotate(-1)
            cnt += 1
        q.popleft()
    else:
        while q[0] != pos:
            q.rotate(1)
            cnt += 1
        q.popleft()

print(cnt)