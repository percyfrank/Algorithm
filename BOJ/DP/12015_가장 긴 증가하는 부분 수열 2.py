
from bisect import bisect_left
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 가장 긴 증가하는 부분 수열을 저장하는 배열
tmp = [arr[0]]

for i in range(n):
    if arr[i] > tmp[-1]:
        tmp.append(arr[i])
    else:
        idx = bisect_left(tmp,arr[i])
        tmp[idx] = arr[i]

print(len(tmp))
