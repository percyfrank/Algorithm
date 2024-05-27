
import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    if s == "pop":
        print(q.pop()) if q else print(-1)
    elif s == "size":
        print(len(q))
    elif s == "empty":
        print(1) if not q else print(0)
    elif s == "top":
        print(q[-1]) if q else print(-1)
    else:
        q.append(int(s.split(" ")[1]))