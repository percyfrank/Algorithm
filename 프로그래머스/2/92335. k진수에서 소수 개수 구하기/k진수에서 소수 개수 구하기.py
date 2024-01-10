def isPrime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
    

def solution(n, k):

    tmp = ""
    while True:
        if n < k:
            tmp += str(n)
            break
        tmp += str(n%k)
        n //= k
    
    answer = 0
    tmp = tmp[::-1].split("0")
    for data in tmp:
        if data == "":
            continue   
        if isPrime(int(data)):
            answer += 1
    
    return answer