def solution(n):
    answer = ''
    
    while n > 0:
        if n < 3:
            answer += str(n)
            break
            
        if n % 3 == 0:
            answer += str(4)
            n -= 1
        else:
            answer += str(n%3)
        n //= 3 
    
    return ''.join(answer[::-1])