from collections import deque

def solution(maps):
    
    dx,dy = [0,1,0,-1],[1,0,-1,0]     
    n,m = len(maps),len(maps[0])

    q = deque([[0,0,1]])
    maps[0][0] = 1
    
    while q:
        x,y,cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = cnt + 1
                q.append((nx,ny,cnt+1))

    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1
