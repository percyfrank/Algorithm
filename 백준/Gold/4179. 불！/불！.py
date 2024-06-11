import sys
from collections import deque

input = sys.stdin.readline


def is_range(x, y):
    return 0 <= x < r and 0 <= y < c


def fire_bfs():
    while fire:
        x, y = fire.popleft()
        for (dx, dy) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x + dx, y + dy
            if not is_range(nx, ny):
                continue
            if not f_visited[nx][ny] and maze[nx][ny] != "#":
                f_visited[nx][ny] = f_visited[x][y] + 1
                fire.append((nx, ny))


def human_bfs():
    while human:
        x, y = human.popleft()
        for (dx, dy) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x + dx, y + dy
            if not is_range(nx, ny):
                print(h_visited[x][y])
                return
            if f_visited[nx][ny] and f_visited[nx][ny] <= h_visited[x][y] + 1:
                continue
            if not h_visited[nx][ny] and maze[nx][ny] != "#":
                h_visited[nx][ny] = h_visited[x][y] + 1
                human.append((nx, ny))
    print("IMPOSSIBLE")
    return


r, c = map(int, input().split())
maze = []
h_visited = [[0] * c for _ in range(r)]
f_visited = [[0] * c for _ in range(r)]
human = deque()
fire = deque()
for i in range(r):
    maze.append(input().rstrip())
    for j in range(c):
        if maze[i][j] == "J":
            human.append((i, j))
            h_visited[i][j] = 1
        elif maze[i][j] == "F":
            fire.append((i, j))
            f_visited[i][j] = 1

fire_bfs()
human_bfs()