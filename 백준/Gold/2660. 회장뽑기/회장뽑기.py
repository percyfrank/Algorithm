from collections import deque

def bfs(start):
    
    q = deque([start])
    visited[start] = 1
    
    while q:
        start = q.popleft()
        for next in graph[start]:
            if not visited[next]:
                visited[next] = visited[start] + 1
                q.append(next)
                
n = int(input())
graph = [[] for _ in range(n+1)]
while True:
    a,b = map(int,input().split())
    if a == b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

max_point = n
ans_list = []
for i in range(1,n+1):
    visited = [0] * (n+1)
    bfs(i)
    ans_list.append((i,max(visited)))
    max_point = min(max_point,max(visited))

ans_list.sort(key=lambda x:(x[1],x[0]))
ans = []
for i in range(n):
    if ans_list[i][1] == max_point:
        ans.append(ans_list[i][0])

print(max_point-1,len(ans))
print(*ans)