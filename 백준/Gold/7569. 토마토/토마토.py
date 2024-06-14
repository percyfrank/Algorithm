import sys
from collections import deque

input = sys.stdin.readline


def is_range(x, y, z):
    return 0 <= x < n and 0 <= y < m and 0 <= z < h


def bfs():
    q = deque()
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if box[k][i][j] == 1:
                    q.append((k, i, j))

    while q:
        z, x, y = q.popleft()
        for (dx, dy, dz) in ((0, 0, 1), (0, 0, -1), (1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0)):
            nx = x + dx
            ny = y + dy
            nz = z + dz
            if not is_range(nx, ny, nz):
                continue
            if box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                q.append((nz, nx, ny))


m, n, h = map(int, input().split())

box = [[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        box[i].append(list(map(int, input().split())))

bfs()

ans = 0
for i in range(h):
    for j in range(n):    
        for k in range(m):
            ans = max(ans, box[i][j][k])
            if box[i][j][k] == 0:
                ans = -1
                break
        else:
            continue
        break
    else:
        continue
    break

print(ans - 1) if ans != -1 else print(ans)