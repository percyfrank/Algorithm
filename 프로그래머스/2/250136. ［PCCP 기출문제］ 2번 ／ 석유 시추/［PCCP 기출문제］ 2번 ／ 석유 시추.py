from collections import deque

def solution(land):
    
    def is_range(x,y):
        return x>=0 and y>=0 and x<n and y<m
    
    def bfs(x,y):
        
        q = deque()
        q.append((x,y))
        cnt = 1
        visited[x][y] = True        
        min_y = max_y = y     
        
        while q:
            x,y = q.popleft()
            min_y = min(y,min_y)
            max_y = max(y,max_y)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not is_range(nx,ny):
                    continue
                if land[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    cnt += 1
        
        for i in range(min_y,max_y+1):
            answer[i] += cnt

    dx,dy = [0,1,0,-1],[1,0,-1,0]
    n,m = len(land),len(land[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    answer = [0] * m
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i,j)

    return max(answer)