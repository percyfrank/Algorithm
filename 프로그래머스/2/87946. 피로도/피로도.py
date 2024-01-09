def solution(k, dungeons):
    
    answer = -1
    def dfs(curr,cnt):
        nonlocal answer
        if cnt > answer:
            answer = cnt
            
        for i in range(n):
            if curr >= dungeons[i][0] and not visited[i]:
                visited[i] = True
                dfs(curr-dungeons[i][1],cnt+1)
                visited[i] = False
    
    n = len(dungeons)
    visited = [False] * n
    dfs(k,0)
    
    return answer