def solution(clothes):
    
    type = dict()
    for n,t in clothes:
        type.setdefault(t,0)
        type[t] += 1
        
    answer = 1
    for value in type.values():
        answer *= (value+1)
    
    return answer-1