def solution(n):
    
    def hanoi(n,start,end,remain):
        
        if n == 1:
            answer.append([start,end])
            return
        
        hanoi(n-1,start,remain,end)
        answer.append([start,end])
        hanoi(n-1,remain,end,start)
    
    answer = []
    hanoi(n,1,3,2)
    
    return answer