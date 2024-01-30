def solution(x, y, n):
    
    dp = [float('inf')] * (3*y+1)
    dp[x] = 0
    
    for i in range(x,y+1):
        dp[i+n] = min(dp[i]+1, dp[i+n])
        dp[i*2] = min(dp[i]+1, dp[i*2])
        dp[i*3] = min(dp[i]+1, dp[i*3])
    
    return dp[y] if dp[y] != float('inf') else -1