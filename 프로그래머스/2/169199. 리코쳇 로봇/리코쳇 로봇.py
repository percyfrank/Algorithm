from collections import deque

def solution(board):
        
    def is_range(x,y):
        return x>=0 and y>=0 and x<n and y<m
                
    def move(x,y,dir):
        while True:
            x += dx[dir]
            y += dy[dir]
            if not is_range(x,y) or board[x][y] == "D":
                break
        x -= dx[dir]
        y -= dy[dir]
        
        return x,y
    
    def bfs(x,y,dis):
        q = deque()
        q.append((x,y,dis))
        
        while q:
            x,y,dis = q.popleft()
            for i in range(4):
                nx,ny = move(x,y,i)
                if (nx,ny) not in visited:
                    visited.add((nx,ny))
                    q.append((nx,ny,dis+1))
                if board[nx][ny] == "G":
                    return dis+1
    
        return -1
                
    answer = 0
    n,m = len(board),len(board[0])
    dx,dy = [0,1,0,-1],[1,0,-1,0]
    visited = set()
        
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                return(bfs(i,j,0))