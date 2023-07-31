
p = int(input())
start = 1

for _ in range(p):
    arr = list(map(int,input().split()))
    if not arr:
        break
    arr = arr[1:]
    tmp = []
    tmp.append(arr[0])
    cnt = 0
    for i in range(1,20):
        if arr[i] > tmp[-1]:
            tmp.append(arr[i])
        else:
            for j in range(len(tmp)):
                if arr[i] < tmp[j]:
                    cnt += len(tmp) - j
                    tmp.insert(j,arr[i])
                    break

    print(start,cnt)
    start += 1




