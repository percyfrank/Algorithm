import sys
from collections import deque

input = sys.stdin.readline


def is_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs():
    q = deque()

    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for (dx, dy) in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = x + dx
            ny = y + dy
            if not is_range(nx, ny):
                continue
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append((nx, ny))


m, n = tuple(map(int, input().split()))
box = [list(map(int, input().split())) for _ in range(n)]

bfs()

ans = 0
for i in range(n):
    ans = max(ans, max(box[i]))
    for j in range(m):
        if box[i][j] == 0:
            ans = -1
            break
    else:
        continue
    break

print(ans - 1) if ans != -1 else print(ans)