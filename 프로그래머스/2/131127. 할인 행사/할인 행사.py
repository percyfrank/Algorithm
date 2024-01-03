from collections import Counter

def solution(want, number, discount):
    
    cnt = {i:j for i,j in zip(want,number)}
    answer = 0
    
    for i in range(len(discount)-9):
        tmp = Counter(discount[i:i+10])
        if tmp == cnt:
            answer += 1
    
    return answer