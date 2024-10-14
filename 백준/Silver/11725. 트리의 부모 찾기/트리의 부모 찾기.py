import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    
    
visited = [0] * (n+1)

def dfs(graph,v,visited):
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(graph,i,visited)            
    
dfs(graph,1,visited)
   
for i in range(2,n+1):
    print(visited[i])