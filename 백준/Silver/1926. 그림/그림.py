import sys
from collections import deque

input = sys.stdin.readline


def is_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y):
    q = deque()
    q.append((x, y))
    cnt = 1
    pictures[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not is_range(nx, ny):
                continue
            if pictures[nx][ny] == 1:
                q.append((nx, ny))
                pictures[nx][ny] = 0
                cnt += 1

    res.append(cnt)


n, m = map(int, input().split())
pictures = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
res = []

for i in range(n):
    for j in range(m):
        if pictures[i][j] == 1:
            bfs(i, j)

print(len(res))
print(max(res) if res else 0)
