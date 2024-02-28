def solution(rows, columns, queries):
    
    maps = [[j*columns + (i+1) for i in range(columns)] for j in range(rows)]    
    answer = []  
    
    for x1,y1,x2,y2 in queries:
        start = maps[x1-1][y1-1]
        MIN = start
        
        for i in range(x1-1,x2-1):
            next = maps[i+1][y1-1]
            maps[i][y1-1] = next
            MIN = min(MIN,next)
        
        for i in range(y1-1,y2-1):
            next = maps[x2-1][i+1]
            maps[x2-1][i] = next
            MIN = min(MIN,next)
        
        for i in range(x2-1,x1-1,-1):
            next = maps[i-1][y2-1]
            maps[i][y2-1] = next
            MIN = min(MIN,next)
        
        for i in range(y2-1,y1-1,-1):
            next = maps[x1-1][i-1]
            maps[x1-1][i] = next
            MIN = min(MIN,next)
        
        maps[x1-1][y1] = start
        answer.append(MIN)
        
    return answer