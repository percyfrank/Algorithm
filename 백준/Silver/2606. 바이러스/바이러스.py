n = int(input())
m = int(input())
computers = [[i] for i in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    computers[a].append(b)
    computers[b].append(a)

visited = [0] * (n+1)
ans = 0

def dfs(start):
    global ans
    
    visited[start] = 1
    for computer in computers[start]:
        if not visited[computer]:
            ans += 1
            dfs(computer)

dfs(1)
print(ans)