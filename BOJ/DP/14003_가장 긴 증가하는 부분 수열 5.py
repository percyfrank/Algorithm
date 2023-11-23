
from bisect import bisect_left
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 가장 긴 증가하는 부분 수열을 저장하는 배열
tmp = [arr[0]]

# dp[i] = i번째 수를 마지막으로 하는 가장 긴 증가 부분 수열의 길이
dp = [0] * n

for i in range(n):
    if arr[i] > tmp[-1]:
        tmp.append(arr[i])
        dp[i] = len(tmp)
    else:
        idx = bisect_left(tmp, arr[i])
        tmp[idx] = arr[i]
        dp[i] = idx + 1

print(len(tmp))

max_len = max(dp)
max_len_pos = dp.index(max_len)
ans = []

while max_len_pos >= 0:
    if dp[max_len_pos] == max_len:
        ans.append(arr[max_len_pos])
        max_len -= 1
    max_len_pos -= 1
print(*ans[::-1])