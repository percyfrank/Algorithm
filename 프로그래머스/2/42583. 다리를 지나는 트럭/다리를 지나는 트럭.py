from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    q = deque([0]*bridge_length)
    curr = 0
    truck_weights.reverse()
    while q:
        answer += 1
        curr -= q.popleft()
        
        if truck_weights:
            if curr + truck_weights[-1] <= weight:
                curr += truck_weights[-1]
                q.append(truck_weights.pop())
            else:
                q.append(0)

    return answer

# 아래 코드는 sum 함수로 인해 시간 초과
# while q:
#     answer += 1
#     q.popleft()
#
#     if truck_weights:
#         if sum(q) + truck_weights[0] <= weight:
#             q.append(truck_weights.pop(0))
#         else:
#             q.append(0)