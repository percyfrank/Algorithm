def solution(name):
    
    alpha = dict()
    for i in range(26):
        alpha[chr(i+65)] = i+1

    MIN = len(name) - 1
    answer = 0
    for i,word in enumerate(name):        
        answer += min(alpha[word]-1,27-alpha[word])
        
        next = i+1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        MIN = min(MIN,2*i+len(name)-next,i+2*(len(name)-next))

    answer += MIN
    
    return answer