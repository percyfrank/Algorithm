import sys

input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().rstrip().split(" ")))
stack = []
answer = [0] * n
towers.reverse()

for idx, h in enumerate(towers):
    while stack and stack[-1][1] < towers[idx]:
        i, prev = stack.pop()
        answer[i] = n - idx
    stack.append((idx, h))

for tower in reversed(answer):
    print(tower, end = " ")