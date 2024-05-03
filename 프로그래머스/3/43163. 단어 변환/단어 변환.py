from collections import deque

def solution(begin, target, words):
        
    def compare(a,b):
        
        cnt = 0      
        for i in range(len(begin)):
            if a[i] != b[i]:
                cnt += 1
        
        return True if cnt == 1 else False
    
    def bfs(word,cnt):
        
        q = deque()
        q.append((word,cnt))
        
        while q:
            word,cnt = q.popleft()
            if word == target:
                return cnt
            for i in range(len(words)):
                if not visited[i] and compare(word,words[i]):
                    q.append((words[i],cnt+1))
                    visited[i] = True
        
    visited = [False] * len(words)            
    if target not in words:
        return 0
    
    return bfs(begin,0)