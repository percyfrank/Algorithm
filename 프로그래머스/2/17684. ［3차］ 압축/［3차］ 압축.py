def solution(msg):
    
    answer = []
    alpha = {chr(65+i):i+1 for i in range(26)}
    
    i,idx = 0,0
    while idx <= len(msg):
        idx += 1
        if idx == len(msg):
            answer.append(alpha[msg[i:idx]])
            break
        
        if msg[i:idx+1] not in alpha:
            answer.append(alpha[msg[i:idx]])
            alpha[msg[i:idx+1]] = len(alpha) + 1
            i = idx
        
    return answer