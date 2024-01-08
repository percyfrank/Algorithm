from collections import deque

def solution(priorities, location):
    
    q = deque(priorities)
    answer = 0
    targer_loc = location
    
    while q:
        MAX = max(q)
        curr = q.popleft()
        targer_loc -= 1
        if curr < MAX:
            q.append(curr)
            if targer_loc < 0:
                targer_loc = len(q)-1
        elif curr == MAX:
            answer += 1
            if targer_loc < 0:
                return answer
                
                