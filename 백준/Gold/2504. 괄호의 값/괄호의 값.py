import sys

input = sys.stdin.readline

strs = input().rstrip()
stack = []
tmp, res = 1, 0

for idx, str in enumerate(strs):
    if str == '(':
        stack.append(str)
        tmp *= 2
    elif str == '[':
        stack.append(str)
        tmp *= 3
    elif str == ')':
        if not stack or stack[-1] == '[':
            res = 0
            break
        if strs[idx-1] == '(':
            res += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == '(':
            res = 0
            break
        if strs[idx-1] == '[':
            res += tmp
        stack.pop()
        tmp //= 3

print(0) if stack else print(res)