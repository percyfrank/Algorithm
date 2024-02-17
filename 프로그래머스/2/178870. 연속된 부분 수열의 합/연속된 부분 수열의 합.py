def solution(sequence, k):

    n = len(sequence) 
    end, subtotal = 0, 0
    answer = []
    for start in range(n):
        
        while subtotal < k and end < n:
            subtotal += sequence[end]
            end += 1
        
        if subtotal == k:
            answer.append([start,end-1])
        
        subtotal -= sequence[start]
    
    answer.sort(key=lambda x:(x[1]-x[0],x[0]))
    
    return answer[0]