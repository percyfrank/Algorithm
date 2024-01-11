def solution(clothes):
    
    type = {}
    for cloth in clothes:
        type.setdefault(cloth[1],1)
        type[cloth[1]]+= 1
        
    answer = 1
    for data in type.values():
        answer *= data
    
    return answer-1