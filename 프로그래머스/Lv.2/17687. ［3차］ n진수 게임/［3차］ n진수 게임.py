def solution(n, t, m, p):
    
    nums = "0123456789ABCDEF"
    
    def makeNum(num):
        
        tmp = ""
        while True:
            q,r = divmod(num,n)
            tmp += nums[r]
            num = q
            if q == 0:
                break

        return tmp[::-1]

    total = ""
    for i in range(t*m):
        total += makeNum(i)
        if len(total) >= t*m:
            break
            
    answer = ""        
    for i in range(p-1,t*m,m):
        answer += total[i]

    return answer