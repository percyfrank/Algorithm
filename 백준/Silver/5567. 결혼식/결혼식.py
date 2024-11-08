n = int(input())
m = int(input())
friends = [[i] for i in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)

visited = [0] * (n+1)
ans = set()
def dfs(start, cnt):
    
    if cnt == 2:
        ans.add(start)
        return        
    
    for friend in friends[start]:
        if not visited[friend]:            
            visited[friend] = 1
        dfs(friend, cnt + 1)
        
dfs(1,0)
print(len(ans)-1)