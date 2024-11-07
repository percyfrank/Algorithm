from collections import deque

def solution(land):
    
    def bfs(x,y):
        nonlocal answer

        q = deque()
        q.append((x,y))
        visited[x][y] = True
        min_y, max_y = y, y
        cnt = 1
        while q:
            x, y = q.popleft()
            min_y = min(min_y,y)
            max_y = max(max_y,y)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and land[nx][ny] == 1:
                        q.append((nx,ny))
                        visited[nx][ny] = True
                        cnt += 1
        
        for i in range(min_y,max_y+1):
            answer[i] += cnt           
    
    m, n = len(land[0]), len(land)    
    dx, dy = [0,1,0,-1], [1,0,-1,0]
    answer = [0] * m
    visited = [[False] * m for _ in range(n)]    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:                
                bfs(i,j)

    return max(answer)
                

 
    
    
    