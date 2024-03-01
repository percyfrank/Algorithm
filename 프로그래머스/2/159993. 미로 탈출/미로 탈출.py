from collections import deque

def solution(maps):
    
    def is_range(x,y):
        return x>=0 and y>=0 and x<n and y<m

    def bfs(start,end):
        
        visited = [[-1 for _ in range(m)] for _ in range(n)]
        q = deque()
        q.append((start[0],start[1]))
        visited[start[0]][start[1]] = 0
        
        while q:
            x,y = q.popleft()
            if x == end[0] and y == end[1]:
                return visited[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if is_range(nx,ny) and maps[nx][ny] != "X" and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))

        return -1            
        
    
    n,m = len(maps), len(maps[0])
    dx,dy = [0,1,0,-1],[1,0,-1,0]
    start,lever,exit = [],[],[]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start = [i,j]
            if maps[i][j] == "L":
                lever = [i,j]
            if maps[i][j] == "E":
                exit = [i,j]
                
    to_lever = bfs(start,lever)
    to_exit = bfs(lever,exit)
    
    return to_lever+to_exit if to_lever != -1 and to_exit != -1 else -1