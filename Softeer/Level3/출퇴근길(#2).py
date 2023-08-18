from collections import deque

n,m = map(int, input().split())

adj = [[] for _ in range(n+1)]
adjR = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    adj[x].append(y)
    adjR[y].append(x)

s,t = map(int,input().split())

def bfs(end,isVisit,adj):
    while q:
        curr = q.popleft()
        if curr == end:
            continue
        for i in range(len(adj[curr])):
            target = adj[curr][i]
            if isVisit[target] == 0:
                isVisit[target] = 1
                q.append(target)

q = deque()
q.append(s)
isVisited1 = [0] * (n+1)
isVisited1[s] = 1
bfs(t,isVisited1,adj)

q.clear()
q.append(t)
isVisited2 = [0] * (n+1)
isVisited2[t] = 1
bfs(s,isVisited2,adj)

q.clear()
q.append(s)
isVisited3 = [0] * (n+1)
bfs(t,isVisited3,adjR)

q.clear()
q.append(t)
isVisited4 = [0] * (n+1)
bfs(s,isVisited4,adjR)

cnt = 0
for i in range(1,n+1):
    if isVisited1[i] == 1 and isVisited2[i] == 1 and isVisited3[i] == 1 and isVisited4[i] == 1:
        cnt += 1
print(cnt-2)

