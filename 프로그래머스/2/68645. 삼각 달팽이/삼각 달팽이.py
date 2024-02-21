def solution(n):
    
    def is_range(x,y):
        return x>=0 and y>=0 and x<n and y<n
    
    arr = [[0 for j in range(1, i+1)] for i in range(1, n+1)]
    dirs = {0 : (0,1), 1 : (1,0), 2 : (-1,-1)}
    x,y,dir = 0,0,1
    arr[x][y] = 1

    for i in range(2,n*(n+1)//2+1):
        nx,ny = x+dirs[dir][0], y+dirs[dir][1]
        if not is_range(nx,ny) or arr[nx][ny] != 0:
            dir = (dir+2) % 3
        nx,ny = x+dirs[dir][0], y+dirs[dir][1]
        arr[nx][ny] = i
        x,y = nx,ny

    answer = []
    for i in arr:
        for j in i:
            if j != 0:
                answer.append(j)  
    
    return answer