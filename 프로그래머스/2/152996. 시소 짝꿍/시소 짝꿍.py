from collections import Counter

def solution(weights):
    answer = 0
    dic = Counter(weights)
    
    for weight in dic:
        answer += (dic[weight] * (dic[weight]-1)) / 2
        answer += dic[weight] * dic[weight*3/2]
        answer += dic[weight] * dic[weight*2]
        answer += dic[weight] * dic[weight*4/3]
    
    return answer