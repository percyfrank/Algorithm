from collections import deque

def solution(people, limit):
    
    answer = 0
    q = deque(sorted(people))

    while q:
        if len(q) == 1:
            q.pop()
            answer += 1
            continue
        if q[0] + q[-1] > limit:
            q.pop()
        else:
            q.pop()
            q.popleft()
        answer += 1
    
    
    return answer