import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int,input().split()))

stack = []
ans = [-1] * n
for i, num in enumerate(numbers):
    while stack and stack[-1][1] < num:
        idx, prev = stack.pop()
        ans[idx] = num
    stack.append((i, num))
    
print(*ans)