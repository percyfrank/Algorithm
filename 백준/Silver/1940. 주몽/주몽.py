n = int(input())
m = int(input())
nums = list(map(int,input().split()))
nums.sort()

start, end = 0, n-1
ans = 0
while start < end:

    if nums[start] + nums[end] == m:
        ans += 1
        start += 1
        end -= 1

    if nums[start] + nums[end] < m:
        start += 1
    elif nums[start] + nums[end] > m:
        end -= 1

print(ans)