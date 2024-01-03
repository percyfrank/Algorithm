from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    cnt = dict()
    for w,n in zip(want,number):
        cnt[w] = n
    
    for i in range(len(discount)-9):
        tmp = Counter(discount[i:i+10])
        if tmp == cnt:
            answer += 1
    
    return answer