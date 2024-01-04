from collections import Counter

def solution(s):
    
    s = s[2:-2]    
    tmp = s.split("},{")

    res = dict()
    for a in tmp:
        a = a.split(",")
        for data in a:
            res.setdefault(data,0)
            res[data] += 1
    
    answer = []
    res = dict(sorted(res.items(),key=lambda x:x[1],reverse=True))
    for key in res.keys():
        answer.append(int(key))
    
    return answer
