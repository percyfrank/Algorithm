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
                
        return x-dx[dir],y-dy[dir]
            
    def bfs(x,y,distance):
        q = deque()
        q.append((x,y,distance))
        visited[x][y] = True
        
        while q:
            x,y,distance = q.popleft()
            if board[x][y] == "G":
                return distance
            for i in range(4):
                nx,ny = move(x,y,i)
                if is_range(nx,ny) and not visited[nx][ny] and board[nx][ny] != "D":
                    q.append((nx,ny,distance+1))
                    visited[nx][ny] = True
        
        return -1

    answer = 0
    dx,dy = [0,1,0,-1],[1,0,-1,0]
    n,m = len(board), len(board[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                answer = bfs(i,j,0)
                
    
    return answer