from collections import deque

m,n = map(int,input().split())


graph = [[0]*m for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int,input().split()))
      
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i,j))   
                
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
                
bfs()
# print(graph)
res = 0

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    res = max(res,max(i))

print(res-1)