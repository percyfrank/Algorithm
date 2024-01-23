from collections import Counter

def solution(topping):
    
    answer = 0
    total = Counter(topping)
    
    cnt = set()
    for t in topping:
        cnt.add(t)
        total[t] -= 1
        if total[t] <= 0:
            del total[t]
        
        if len(cnt) == len(total):
            answer += 1

    return answer