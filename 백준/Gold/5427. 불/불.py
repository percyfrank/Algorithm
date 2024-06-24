import sys
from collections import deque

input = sys.stdin.readline


def is_range(x,y):
    return 0 <= x < h and 0 <= y < w


def fire_bfs():

    while fire:
        x, y = fire.popleft()
        for (dx, dy) in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = x + dx
            ny = y + dy
            if not is_range(nx, ny):
                continue
            if buildings[nx][ny] != "#" and not fire_visited[nx][ny]:
                fire_visited[nx][ny] = fire_visited[x][y] + 1
                fire.append((nx, ny))


def human_bfs():

    while human:
        x, y = human.popleft()
        for (dx, dy) in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = x + dx
            ny = y + dy
            if not is_range(nx, ny):
                print(human_visited[x][y])
                return
            if fire_visited[nx][ny] and fire_visited[nx][ny] <= human_visited[x][y] + 1:
                continue
            if buildings[nx][ny] != "#" and not human_visited[nx][ny]:
                human_visited[nx][ny] = human_visited[x][y] + 1
                human.append((nx, ny))

    print("IMPOSSIBLE")
    return

t = int(input())
for _ in range(t):
    w, h = tuple(map(int, input().split()))
    buildings = []
    for i in range(h):
        buildings.append(input().rstrip())
    human_visited = [[0] * w for _ in range(h)]
    fire_visited = [[0] * w for _ in range(h)]
    human = deque()
    fire = deque()

    for i in range(h):
        for j in range(w):
            if buildings[i][j] == "@":
                human.append((i, j))
                human_visited[i][j] = 1
            elif buildings[i][j] == "*":
                fire.append((i, j))
                fire_visited[i][j] = 1

    fire_bfs()
    human_bfs()