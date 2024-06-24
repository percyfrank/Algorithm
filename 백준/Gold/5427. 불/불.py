import sys
from collections import deque

input = sys.stdin.readline

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def is_range(x,y):
    return 0 <= x < h and 0 <= y < w


def fire_bfs():
    while fire:
        x, y, cnt = fire.popleft()
        for (dx, dy) in dirs:
            nx = x + dx
            ny = y + dy
            if not is_range(nx, ny):
                continue
            if buildings[nx][ny] != "#" and not visited[nx][ny]:
                visited[nx][ny] = cnt + 1
                fire.append((nx, ny, cnt+1))

def human_bfs():
    while human:
        x, y, cnt = human.popleft()
        for (dx, dy) in dirs:
            nx = x + dx
            ny = y + dy
            if not is_range(nx, ny):
                print(cnt)
                return
            if buildings[nx][ny] != "#":
                if cnt + 1 < visited[nx][ny] or not visited[nx][ny]:
                    visited[nx][ny] = -1
                    human.append((nx, ny, cnt+1))

    print("IMPOSSIBLE")
    return

t = int(input())
for _ in range(t):
    w, h = tuple(map(int, input().split()))
    buildings = []
    for i in range(h):
        buildings.append(input().rstrip())
    visited = [[0] * w for _ in range(h)]
    human = deque()
    fire = deque()

    for i in range(h):
        for j in range(w):
            if buildings[i][j] == "*":
                fire.append((i, j, 1))
                visited[i][j] = 1
            elif buildings[i][j] == "@":
                human.append((i, j, 1))

    fire_bfs()
    human_bfs()