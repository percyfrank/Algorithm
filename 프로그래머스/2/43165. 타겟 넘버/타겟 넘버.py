def solution(numbers, target):
    
    def dfs(idx,result):
        
        nonlocal answer
        
        if idx == n:
            if result == target:
                answer += 1
            return
        
        dfs(idx+1,result+numbers[idx])
        dfs(idx+1,result-numbers[idx])

    answer = 0
    n = len(numbers)
    dfs(0,0)
    
    return answer