from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    
    heapify(scoville)
    while len(scoville) > 1:
        if scoville[0] >= K:
            return answer
        a = heappop(scoville)
        b = heappop(scoville)
        heappush(scoville, a + b*2)
        answer += 1
    
    return -1 if scoville[0] < K else answer
    
