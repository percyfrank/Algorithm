def solution(numbers):
    answer = [-1] * len(numbers)
    stack_idx = []
    
    for i in range(len(numbers)):
        while stack_idx and numbers[stack_idx[-1]] < numbers[i]:
            answer[stack_idx.pop()] = numbers[i]
        
        stack_idx.append(i)
    
    return answer