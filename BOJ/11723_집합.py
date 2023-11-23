import sys
input = sys.stdin.readline

m = int(input())
s = set()

while True:
    arr = input().rstrip().split()
    if not arr:
        break
    if arr[0] != 'all' and arr[0] != 'empty':
        arr[1] = int(arr[1])

    if arr[0] == 'add':
        s.add(arr[1])
    elif arr[0] == 'remove' and arr[1] in s:
        s.remove(arr[1])
    elif arr[0] == 'check':
        if arr[1] in s:
            print(1)
        else:
            print(0)
    elif arr[0] == 'toggle':
        if arr[1] in s:
            s.remove(arr[1])
        else:
            s.add(arr[1])
    elif arr[0] == 'all':
        s = set(range(1,21))
    elif arr[0] == 'empty':
        s.clear()



