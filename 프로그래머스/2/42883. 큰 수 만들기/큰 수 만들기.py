def solution(number, k):
    
    answer = []
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
            
        answer.append(num)
        
    return "".join(answer) if k == 0 else "".join(answer[:-1])