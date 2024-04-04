from collections import deque

def solution(n, wires):
    
    def bfs(start):
        
        visited = [False] * (n+1)
        q = deque()
        q.append(start)
        visited[start] = True
        cnt = 1
        
        while q:
            idx = q.popleft()
            for i in tmp_wires[idx]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
                    cnt += 1
                    
        return cnt
        
    
    tmp_wires = [[] for _ in range(n+1)]
    for v1,v2 in wires:
        tmp_wires[v1].append(v2)
        tmp_wires[v2].append(v1)
    
    answer = float('inf')
    for a,b in wires:
        tmp_wires[a].remove(b)
        tmp_wires[b].remove(a)
        
        answer = min(answer,abs(bfs(a)-bfs(b)))
        
        tmp_wires[a].append(b)
        tmp_wires[b].append(a)
    
    
    return answer