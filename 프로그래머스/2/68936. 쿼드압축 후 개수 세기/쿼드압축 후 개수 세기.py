def solution(arr):
    
    answer = [0,0]
    def quad(x,y,length):
        start = arr[x][y]
        for i in range(x,x+length):
            for j in range(y,y+length):
                if arr[i][j] != start:
                    length //= 2
                    quad(x,y,length)
                    quad(x,y+length,length)
                    quad(x+length,y,length)
                    quad(x+length,y+length,length)
                    return
        answer[start] += 1
    
    quad(0,0,len(arr))
    
    return answer