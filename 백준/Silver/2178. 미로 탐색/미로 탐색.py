import sys
from collections import deque

input = sys.stdin.readline


def is_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for (dx, dy) in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = x + dx
            ny = y + dy
            if not is_range(nx, ny):
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx, ny))

    return maze[n - 1][m - 1]


n, m = tuple(map(int, input().split()))
maze = [list(map(int, input().rstrip())) for _ in range(n)]
print(bfs(0, 0))