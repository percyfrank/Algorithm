


n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
arrR = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    arr[x].append(y)
    arrR[y].append(x)

s, t = map(int, input().split())

def dfs(now, arr, visit):
    if visit[now] == 1:
        return
    visit[now] = 1
    for neighbor in arr[now]:
        dfs(neighbor, arr, visit)
    return

fromS = [0] *(n+1)
fromS[t] = 1
dfs(s, arr, fromS)

fromT = [0] * (n+1)
fromT[s] = 1
dfs(t, arr, fromT)

toS = [0] * (n+1)
dfs(s, arrR, toS)

toT = [0] * (n+1)
dfs(t, arrR, toT)

count = 0
for i in range(1,n+1):
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        count += 1

print(count-2)