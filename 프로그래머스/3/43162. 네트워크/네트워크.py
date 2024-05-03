from collections import deque

def solution(n, computers):
    
    def bfs(node):
        
        q = deque([node])
        visited[node] = True
        
        while q:
            node = q.popleft()
            for i in range(n):
                if not visited[i] and computers[i][node] == 1:
                    visited[i] = True
                    bfs(i)    
    
    visited = [False] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    
    return answer