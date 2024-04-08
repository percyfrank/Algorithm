from collections import deque
import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def is_range(x,y):
    return x>=0 and y>=0 and x<n and y<n

def bfs(x,y):

    q = deque()
    q.append((x,y))
    color = maps[x][y]
    visited[x][y] = True

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_range(nx,ny) and not visited[nx][ny] and maps[nx][ny] == color:
                visited[nx][ny] = True
                q.append((nx,ny))

    return

n = int(input())
maps = [list(input()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt += 1

visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if maps[i][j] == "R":
            maps[i][j] = "G"
cnt_b = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt_b += 1

print(cnt, cnt_b)