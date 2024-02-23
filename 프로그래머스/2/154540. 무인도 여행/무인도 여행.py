from collections import deque

def solution(maps):
    
    def is_range(x,y):
        return x>=0 and y>=0 and x<n and y<m
    
    def bfs(x,y):
        q = deque()
        q.append((x,y))                  
        cnt = int(maps[x][y])
        visited[x][y] = True        
        while q:
            x,y = q.popleft() 
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if is_range(nx,ny) and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    cnt += int(maps[nx][ny])
                    q.append((nx,ny))

        return cnt
        
    answer = []
    n,m = len(maps),len(maps[0])
    visited = [[False]*m for _ in range(n)]
    dx,dy = [0,1,0,-1],[1,0,-1,0]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(i,j))
        
    return sorted(answer) if answer else [-1]