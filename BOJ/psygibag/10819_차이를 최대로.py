from itertools import permutations

n = int(input())
arr = list(map(int,input().split()))

total = list(permutations(arr,n))

MAX = 0
for a in total:
    tmp = 0
    for i in range(len(a)-1):
        tmp += abs(a[i] - a[i+1])
    MAX = max(tmp,MAX)

print(MAX)
