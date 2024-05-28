import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
q = deque()

for _ in range(n):
    s = input().rstrip()
    if s == "pop":
        print(q.popleft()) if q else print(-1)
    elif s == "size":
        print(len(q))
    elif s == "empty":
        print(1) if not q else print(0)
    elif s == "front":
        print(q[0]) if q else print(-1)
    elif s == "back":
        print(q[-1]) if q else print(-1)
    else:
        s, num = s.split(" ")
        q.append(num)