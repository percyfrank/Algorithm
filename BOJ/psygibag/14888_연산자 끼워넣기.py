from itertools import permutations

n = int(input())
nums = list(map(int,input().split()))
tmps = list(map(int,input().split()))

cal = {}
cal[0] = '+'
cal[1] = '-'
cal[2] = '*'
cal[3] = '/'

cals = []
for i in range(4):
    while tmps[i] != 0:
        cals.append(cal[i])
        tmps[i] -= 1

arrs = list(permutations(cals,len(cals)))

MAX = -float('inf')
MIN = float('inf')

for arr in arrs:
    result = nums[0]
    for i in range(1,n):
        if arr[i-1] == '+':
            result += nums[i]
        elif arr[i-1] == '-':
            result -= nums[i]
        elif arr[i-1] == '*':
            result *= nums[i]
        else:
            if result < 0 and nums[i] > 0:
                result = -((-result) // nums[i])
            else:
                result //= nums[i]
    MAX = max(MAX,result)
    MIN = min(MIN,result)

print(MAX)
print(MIN)













