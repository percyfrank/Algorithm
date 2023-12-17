from collections import deque

def solution(land):

    def bfs(x,y,land):
        q = deque()
        q.append((x,y))
        visited[x][y] = 1

        cnt = 1
        min_y, max_y = y,y

        while q:
            x,y = q.popleft()
            min_y = min(min_y,y)
            max_y = max(max_y,y)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= len(land) or ny >= len(land[0]):
                    continue
                if land[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    cnt += 1

        for i in range(min_y, max_y+1):
            total[i] += cnt
        
    n = len(land)
    m = len(land[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    total = [0 for _ in range(m)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                bfs(i,j,land)
    
    return max(total)