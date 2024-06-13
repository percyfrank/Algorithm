import sys
from collections import deque

input = sys.stdin.readline


def is_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    color = maps[x][y]

    while q:
        x, y = q.popleft()
        for (dx, dy) in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = x + dx
            ny = y + dy
            if not is_range(nx, ny):
                continue
            if maps[nx][ny] == color and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))


n = int(input())
maps = [list(input().rstrip()) for _ in range(n)]
m = len(maps[0])

cnt = 0
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            bfs(i, j)
            cnt += 1

for i in range(n):
    for j in range(m):
        if maps[i][j] == "G":
            maps[i][j] = "R"

visited = [[0] * m for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            bfs(i, j)
            cnt2 += 1

print(cnt, cnt2)