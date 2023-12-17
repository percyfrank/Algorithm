def solution(s):
    answer = True
    
    s = list(s)
    tmp = []
    
    for a in s:
        if a == "(":
            tmp.append(a)
        else:
            if tmp:
                tmp.pop()
            else:
                answer = False
                break
                
    if tmp:
        answer = False

    return answer