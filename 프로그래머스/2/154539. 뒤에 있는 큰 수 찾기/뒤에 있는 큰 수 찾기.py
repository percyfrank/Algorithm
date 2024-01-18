from heapq import heappush, heappop

def solution(numbers):
    
    answer = [-1] * len(numbers)
    h = []
    
    for i in range(len(numbers)):
        while h and h[0][0] < numbers[i]:
            answer[heappop(h)[1]] = numbers[i]
    
        heappush(h,(numbers[i],i))
        
    return answer