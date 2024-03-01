from collections import deque
from math import factorial

def solution(n, k):
    
    arr = deque([i for i in range(1,n+1)])
    answer = []

    while arr:
        num = (k-1) // factorial(n-1)
        answer.append(arr[num])
        arr.remove(arr[num])
        
        k %= factorial(n-1)
        n -= 1
        
    return answer