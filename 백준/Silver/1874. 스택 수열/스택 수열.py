
import sys
input = sys.stdin.readline
n = int(input())

stack = []
answer = []
num = 1

for _ in range(n):
    target = int(input())
    while num <= target:
        stack.append(num)
        num += 1
        answer.append("+")
    if stack[-1] == target:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        answer = []
        break

if answer:
    for data in answer:
        print(data)