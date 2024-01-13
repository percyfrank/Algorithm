def solution(n, t, m, p):
    
    nums = "0123456789ABCDEF"
    
    def makeNum(num):
        
        tmp = ""
        while True:
            if num < n:
                tmp += nums[num]
                break
            tmp += nums[num % n]
            num //= n
            
        return tmp[::-1]

    answer = total = ""
    start = 0
    while True:
        if len(total) >= t*m:
            while t > 0:
                answer += total[p-1]
                p += m
                t -= 1
            break
        
        total += makeNum(start)
        start += 1

    return answer