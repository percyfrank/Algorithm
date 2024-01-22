def solution(prices):
    
    answer = [len(prices)-i-1 for i in range(len(prices))]
    stack = []
    for i in range(len(prices)):
        
        while stack and stack[-1][1] > prices[i]:
            idx,price = stack.pop()
            answer[idx] = i-idx
        
        stack.append((i,prices[i]))
    
    return answer