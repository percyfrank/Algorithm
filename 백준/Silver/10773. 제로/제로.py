
import sys
from collections import deque

k = int(sys.stdin.readline())
q = deque()

for _ in range(k):
    n = int(sys.stdin.readline())
    q.pop() if n == 0 else q.append(n)

print(sum(q))