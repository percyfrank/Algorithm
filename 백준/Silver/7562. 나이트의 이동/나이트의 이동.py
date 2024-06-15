import sys
from collections import deque

input = sys.stdin.readline


def is_range(x, y):
    return 0 <= x < l and 0 <= y < l


def bfs(x, y):
    q = deque()
    q.append((x, y))
    chess[x][y] = 1

    while q:
        x, y = q.popleft()
        if x == target_x and y == target_y:
            return chess[x][y]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if not is_range(nx, ny):
                continue
            if not chess[nx][ny]:
                chess[nx][ny] = chess[x][y] + 1
                q.append((nx, ny))


t = int(input())
for _ in range(t):
    l = int(input())
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    chess = [[0] * l for _ in range(l)]
    start_x, start_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    cnt = bfs(start_x, start_y)
    print(cnt - 1)