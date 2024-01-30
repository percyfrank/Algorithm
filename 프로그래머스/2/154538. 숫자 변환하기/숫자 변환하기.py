def solution(x, y, n):
    
    dp = [1000001] * (y+1)
    dp[y] = 0
    for i in range(y,x-1,-1):
        dp[i-n] = min(dp[i-n], dp[i] + 1)
        if i % 2 == 0:
            dp[i//2] = min(dp[i]+1, dp[i//2])
        if i % 3 == 0:
            dp[i//3] = min(dp[i]+1, dp[i//3])
    
    return dp[x] if dp[x] != 1000001 else -1