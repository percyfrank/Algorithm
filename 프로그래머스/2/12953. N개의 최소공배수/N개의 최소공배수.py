def solution(arr):
    
    def gcd(a,b):
        while b > 0:
            a,b = b,a%b
        return a
    
    answer = arr[0]
    for num in arr:
        answer = (answer * num) / gcd(answer,num)
    
    return answer
