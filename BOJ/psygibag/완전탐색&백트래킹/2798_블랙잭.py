from itertools import combinations

n,m = map(int,input().split())
arr = list(map(int,input().split()))
totals = list(combinations(arr,3))
MAX = 0

for total in totals:
    tmp = sum(total)
    if tmp <= m:
        MAX = max(MAX,tmp)

print(MAX)


