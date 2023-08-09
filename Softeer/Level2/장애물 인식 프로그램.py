import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(input().rstrip()))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = []

def bfs(x,y):
    q = deque()
    q.append((x,y))
    arr[x][y] = -1
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if arr[nx][ny] == '1':
                    arr[nx][ny] = -1
                    cnt += 1
                    q.append((nx,ny))
    result.append(cnt)

for i in range(n):
    for j in range(n):
        if arr[i][j] == '1':
            bfs(i,j)

print(len(result))
result.sort()
for data in result:
    print(data)