
n = int(input())
arr = list(map(int,input().split()))

# dp[i] = i번째 수를 마지막으로 하는 가장 긴 증가 부분 수열의 길이
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

# 가장 긴 증가하는 부분 수열의 길이
max_len = max(dp)
max_len_pos = dp.index(max_len)
tmp = []

while max_len_pos >= 0:
    if dp[max_len_pos] == max_len:
        tmp.append(arr[max_len_pos])
        max_len -= 1
    max_len_pos -= 1

tmp.reverse()
print(*tmp)


