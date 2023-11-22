
n = int(input())
arr = list(map(int, input().split()))

# dp[i] = i번째 수를 마지막 원소로 가지는 증가하는 부분 수열의 합
dp = arr[:]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(dp)
