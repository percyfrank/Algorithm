from collections import deque

n,m = map(int, input().split())

adj = [[] for _ in range(n+1)]
adjR = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    adj[x].append(y)
    adjR[y].append(x)

s,t = map(int,input().split())

def bfs(start, isVisit, adj):
    q = deque()
    q.append(start)
    isVisit[start] = 1
    while q:
        curr = q.popleft()
        for target in adj[curr]:
            if isVisit[target] == 0:
                isVisit[target] = 1
                q.append(target)

isVisited1 = [0] * (n+1)
isVisited1[t] = 1
bfs(s, isVisited1, adj)

isVisited2 = [0] * (n+1)
isVisited2[s] = 1
bfs(t, isVisited2, adj)

isVisited3 = [0] * (n+1)
bfs(s, isVisited3, adjR)

isVisited4 = [0] * (n+1)
bfs(t, isVisited4, adjR)

cnt = 0
for i in range(1,n+1):
    if isVisited1[i] and isVisited2[i] and isVisited3[i] and isVisited4[i]:
        cnt += 1
print(cnt-2)
