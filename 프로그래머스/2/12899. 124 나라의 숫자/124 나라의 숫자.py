def solution(n):
    
    answer = ''
    while n > 0:
        q,r = divmod(n,3)
        if r == 0:
            r = 4
            q -= 1
        answer += str(r)
        n = q
    
    return answer[::-1]