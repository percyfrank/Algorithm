n = int(input())
arr = list(map(int, input().split()))

result = [-1] * n
stackIdx = []
for i in range(len(arr)):
    while stackIdx and arr[stackIdx[-1]] < arr[i]:
        result[stackIdx.pop()] = arr[i]
    stackIdx.append(i)

print(*result)