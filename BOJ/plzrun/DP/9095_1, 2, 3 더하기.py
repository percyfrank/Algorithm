

t = int(input())

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(t):
    n = int(input())
    print(dp[n])

# n-1에서 + 1 -> n-1을 만드는 경우의 수 = dp[n-1]
# n-2에서 + 2 -> N-2를 만드는 경우의 수 = dp[n-2]
# n-3에서 + 3 -> n-3을 만드는 경우의 수 = dp[n-3]









