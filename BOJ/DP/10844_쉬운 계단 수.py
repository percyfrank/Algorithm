
n = int(input())

dp = [0] * 101
dp[1] = 9
dp[2] = 17

for i in range(3, n+1):
    dp[i] = dp[i-1] * 2 - (i-1)

print(dp[n] % 1000000000)