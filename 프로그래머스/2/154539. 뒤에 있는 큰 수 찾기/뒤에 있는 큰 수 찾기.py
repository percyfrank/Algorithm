def solution(numbers):
    
    answer = [-1] * len(numbers)
    stack_idx = []
    
    for i in range(len(numbers)):
        while stack_idx and stack_idx[-1][1] < numbers[i]:
            idx,num = stack_idx.pop()
            answer[idx] = numbers[i]
        
        stack_idx.append((i,numbers[i]))
    
    return answer