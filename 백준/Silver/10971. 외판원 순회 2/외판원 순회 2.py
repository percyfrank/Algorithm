import sys
input = sys.stdin.readline

def backtracking(start, curr_idx, cnt, sum):
    global ans
    
    if sum > ans:
        return
    
    if cnt == n and nums[curr_idx][start]:
        sum += nums[curr_idx][start]
        ans = min(ans,sum)
        return
    
    for i in range(n):
        if not visited[i] and nums[curr_idx][i]:
            visited[i] = True
            backtracking(start, i, cnt+1, sum+nums[curr_idx][i])
            visited[i] = False

n = int(input())
nums = [list(map(int,input().split())) for _ in range(n)]
visited = [False] * n
ans = float('inf')

for i in range(n):
    visited[i] = True
    backtracking(i,i,1,0)
    visited[i] = False
    
print(ans) 