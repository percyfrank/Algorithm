def solution(n):
    answer = ''
    rule = "124"
    
    while n > 0:
        n -= 1
        answer += rule[n%3]
        n //= 3
    
    return answer[::-1]