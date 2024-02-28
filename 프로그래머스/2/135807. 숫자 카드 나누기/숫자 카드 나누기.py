def solution(arrayA, arrayB):
    answer = 0
    
    def gcd(a,b):
        while b>0:
            a,b = b,a%b
        return a
    
    a = arrayA[0]
    for i in arrayA:
        a = gcd(a,i)
    
    flag = True
    for i in arrayB:
        if i % a == 0:
            flag = False
            break
    if flag:
        answer = max(answer,a)
    
    b = arrayB[0]
    for i in arrayB:
        b = gcd(b,i)
    
    flag = True
    for i in arrayA:
        if i % b == 0:
            flag = False
            break
    if flag:
        answer = max(answer,b)
    
    return answer