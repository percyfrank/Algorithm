def solution(dirs):
    
    tmp = set()
    x,y = 0,0
    for dir in dirs:
        
        if dir == "U":
            nx,ny = x, y+1
        elif dir == "D":
            nx,ny = x, y-1
        elif dir == "R":
            nx,ny = x+1, y
        elif dir == "L":
            nx,ny = x-1, y
            
        if -5 <= nx <= 5  and -5 <= ny <= 5:
            tmp.add((x,y,nx,ny))
            tmp.add((nx,ny,x,y))
            x,y = nx,ny    

    
    return len(tmp) // 2