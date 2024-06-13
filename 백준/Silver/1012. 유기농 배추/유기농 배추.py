import sys
from collections import deque

input = sys.stdin.readline


def is_range(x, y):
    return 0 <= x < m and 0 <= y < n


def bfs(x, y):
    q = deque()
    q.append((x, y))
    maps[x][y] = 0

    while q:
        x, y = q.popleft()
        for (dx, dy) in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = x + dx
            ny = y + dy
            if not is_range(nx, ny):
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = 0
                q.append((nx, ny))


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    maps = [[0] * n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        maps[x][y] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)