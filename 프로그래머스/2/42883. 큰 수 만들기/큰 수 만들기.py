def solution(number, k):
    
    answer = []
    for num in number:
        
        while answer and answer[-1] < num and k > 0:
            answer.pop()
            k -= 1
        
        answer.append(num)
    
    return ''.join(answer) if k == 0 else ''.join(answer[:-k])