from collections import deque

def solution(maps):
    
    def is_range(x,y):
        return x>=0 and y>=0 and x<n and y<m
    
    def bfs(start,end,dis):
        
        visited = [[0 for _ in range(m)] for _ in range(n)]
        q = deque()
        q.append((start[0],start[1],dis))
        visited[start[0]][start[1]] = True
        
        while q:
            x,y,dis = q.popleft()
            if x == end[0] and y == end[1]:
                return dis
            for dx,dy in ((0,1),(1,0),(0,-1),(-1,0)):
                nx = x + dx
                ny = y + dy
                if not is_range(nx,ny):
                    continue
                if maps[nx][ny] != "X" and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny,dis+1))
        return -1            

    n,m = len(maps),len(maps[0])
    start,lever,end = [],[],[]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start = [i,j]
            elif maps[i][j] == "L":
                lever = [i,j]
            elif maps[i][j] == "E":
                end = [i,j]
    
    to_lever = bfs(start,lever,0)
    to_end = bfs(lever,end,0)
    
    return to_lever + to_end if (to_lever != -1 and to_end != -1) else -1