import sys

input = sys.stdin.readline

n = int(input())
answer = 0
for _ in range(n):
    word = input().rstrip()
    stack = []
    for w in word:
        if stack and stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)

    if not stack:
        answer += 1

print(answer)