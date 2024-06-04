import sys
from collections import deque

input = sys.stdin.readline


def is_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y):
    q = deque()
    visited[x][y] = True
    cnt = 1
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_range(nx, ny):
                if pictures[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    cnt += 1
                    q.append((nx, ny))

    return cnt


n, m = tuple(map(int, input().split(" ")))
pictures = [list(map(int, input().split(" "))) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

res = []
for i in range(n):
    for j in range(m):
        if pictures[i][j] == 1 and not visited[i][j]:
            cnt = bfs(i, j)
            res.append(cnt)

print(len(res))
print(max(res)) if res else print(0)