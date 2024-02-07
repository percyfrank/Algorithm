def solution(sequence, k):
    
    answer = []
    right = 0
    subtotal = 0
    
    for left in range(len(sequence)):
        
        while subtotal < k and right < len(sequence):
            subtotal += sequence[right]
            right += 1
            
        if subtotal == k:
            answer.append([left,right-1, right-left-1])
            
        subtotal -= sequence[left]
    
    answer.sort(key=lambda x:(x[2],x[0]))
    
    return [answer[0][0],answer[0][1]]
