from collections import deque

def solution(begin, target, words):
        
    def compare(a,b):
        
        cnt = 0      
        for i in range(n):
            if a[i] != b[i]:
                cnt += 1
        
        return True if cnt == 1 else False
    
    def dfs(idx,cnt):
        
        q = deque()
        q.append((idx,cnt))
        visited[idx] = True
        
        while q:
            idx,cnt = q.popleft()
            if words[idx] == target:
                return cnt
            for i in range(m):
                if not visited[i] and compare(words[idx],words[i]):
                    q.append((i,cnt+1))
                    visited[i] = True
                    
        return 0
        
    answer = 0
    n,m = len(begin),len(words)
    visited = [False] * m
    
    for i in range(m):
        if not visited[i] and compare(begin,words[i]):
            answer = dfs(i,1)
    
    return answer