import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()
    if arr == "[]":
        arr = deque([])
    else:
        arr = arr.replace("[", "").replace("]", "").split(",")
        arr = deque(arr)

    dir = True
    errorFlag = True
    for i in range(len(p)):
        if p[i] == "R":
            dir = not dir
        else:
            if not arr:
                print("error")
                errorFlag = False
                break
            arr.popleft() if dir else arr.pop()

    if errorFlag and dir:
        print('[' + ','.join(arr) + ']')
    elif errorFlag and not dir:
        arr.reverse()
        print('[' + ','.join(arr) + ']')