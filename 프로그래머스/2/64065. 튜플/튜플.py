from collections import Counter

def solution(s):
    
    s = s[2:-2].split("},{")

    res = dict()
    for t in s:
        tmp = list(map(int, t.split(",")))
        for data in tmp:
            res.setdefault(data,0)
            res[data] += 1
    
    answer = []
    res = dict(sorted(res.items(),key=lambda x:x[1],reverse=True))
    for key in res.keys():
        answer.append(key)
    
    return answer

