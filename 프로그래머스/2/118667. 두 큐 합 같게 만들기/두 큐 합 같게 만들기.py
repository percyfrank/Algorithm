from collections import deque

def solution(queue1, queue2):
    
    total = sum(queue1+queue2)
    if total % 2 != 0:
        return -1
    target = total // 2
    
    q1 = sum(queue1)
    queue1, queue2 = deque(queue1), deque(queue2)
    answer = 0
    while True:
        if not queue1 or not queue2:
            return -1
        
        if q1 == target:
            return answer
        elif q1 > target:
            q1 -= queue1.popleft()
        elif q1 < target:
            tmp = queue2.popleft()
            q1 += tmp
            queue1.append(tmp)
        answer += 1
