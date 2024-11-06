import sys
input = sys.stdin.readline

n = int(input())
buildings = [int(input()) for _ in range(n)]

stack = []
cnt = 0
for i,curr_height in enumerate(buildings):
    while stack and stack[-1][1] <= curr_height:
        idx, h = stack.pop()
        cnt += (i-idx-1)
    stack.append((i,curr_height))

for i,height in stack:
    cnt += (n-i-1)
    
print(cnt)
