def solution(brown, yellow):
    answer = []
    
    tot = brown + yellow
    for i in range(1,tot+1):
        if tot % i == 0:
            a = i
            b = tot // i
            tmp = 4 + (a-2)*2 + (b-2)*2
            if tmp == brown:
                answer.append(a)
                answer.append(b)
                break
    
    answer.sort(reverse=True)
    return answer