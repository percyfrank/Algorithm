def solution(numbers, target):
    
    
    def dfs(idx,total):
        nonlocal answer
        
        if idx == len(numbers):
            if total == target:
                answer += 1
            return
        
        dfs(idx+1,total+numbers[idx])
        dfs(idx+1,total-numbers[idx])
            
    answer = 0
    dfs(0,0)
    
    return answer