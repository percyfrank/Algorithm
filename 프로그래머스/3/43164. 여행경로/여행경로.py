def solution(tickets):
    
    def dfs(node,path):
        
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return
        
        for idx,(start,end) in enumerate(tickets):
            if not visited[idx] and start == node:
                visited[idx] = True
                dfs(end,path+[end])
                visited[idx] = False
    
    answer = []
    visited = [False] * len(tickets)
    
    dfs("ICN",["ICN"])
    
    return sorted(answer)[0]