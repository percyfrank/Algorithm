def solution(clothes):
    
    cnt = dict()
    for cloth in clothes:
        cnt.setdefault(cloth[1],0)
        cnt[cloth[1]] += 1
        
    answer = 1
    for key,value in cnt.items():
        answer *= (value+1)
    
    return answer-1