def backtracking(idx,sum):
    global cnt
    
    if idx >= n:
        return
    sum += nums[idx]
    if sum == s:
        cnt += 1
       
    backtracking(idx+1,sum)
    backtracking(idx+1,sum-nums[idx])
    
n,s = map(int,input().split())
nums = list(map(int,input().split()))
cnt = 0

backtracking(0,0)
print(cnt)