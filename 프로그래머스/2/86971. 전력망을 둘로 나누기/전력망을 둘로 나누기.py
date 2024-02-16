from collections import deque

def solution(n, wires):
    
    tmp_wire = [[] for _ in range(n+1)]
    for a,b in wires:
        tmp_wire[a].append(b)
        tmp_wire[b].append(a)
    
    def bfs(start):
        q = deque()
        q.append(start)
        visited[start] = True
        cnt = 1
        
        while q:
            start = q.popleft()            
            for i in tmp_wire[start]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
                    cnt += 1
        return cnt

    answer = n
    for v1,v2 in wires:
        tmp_wire[v1].remove(v2)
        tmp_wire[v2].remove(v1)
        
        cnt = 0
        visited = [False for _ in range(n+1)]  
        answer = min(answer,abs(bfs(v1)-bfs(v2)))
        
        tmp_wire[v1].append(v2)
        tmp_wire[v2].append(v1)
        

    return answer