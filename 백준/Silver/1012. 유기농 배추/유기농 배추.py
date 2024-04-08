from collections import deque
import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def is_range(x,y):
    return x>=0 and y>=0 and x<n and y<m

def bfs(x,y):
    global cnt

    cnt += 1
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_range(nx,ny) and not visited[nx][ny]:
                if maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx,ny))
    return


t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())    # 가로(m) 10, 세로(n) 8
    maps = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        y,x = map(int,input().split())
        maps[x][y] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1 and not visited[i][j]:
                bfs(i,j)

    print(cnt)