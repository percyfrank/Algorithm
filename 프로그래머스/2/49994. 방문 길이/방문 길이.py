def solution(dirs):
    
    tmp = set()
    d = {'U' : (0,1),'D' : (0,-1),'R' : (1,0),'L' : (-1,0)}
    
    x,y = 0,0
    for dir in dirs:
        nx,ny = x+d[dir][0], y+d[dir][1]
            
        if -5 <= nx <= 5  and -5 <= ny <= 5:
            tmp.add((x,y,nx,ny))
            tmp.add((nx,ny,x,y))
            x,y = nx,ny    

    return len(tmp) // 2