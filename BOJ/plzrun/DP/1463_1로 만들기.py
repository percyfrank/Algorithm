
n = int(input())

# 문제 입력 조건이 n >= 1인 정수 -> dp[1]까지만 할당 가능
dp = [0] * (n+1)
dp[1] = 0

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[n])