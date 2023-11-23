
n,m = map(int,input().split())

chart = []
for _ in range(n):
    chart.append(list(map(int,input().split())))

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + chart[i-1][j-1]

for _ in range(m):
    x,y,X,Y = map(int,input().split())
    result = dp[X][Y] - dp[X][y-1] - dp[x-1][Y] + dp[x-1][y-1]
    print(result)


