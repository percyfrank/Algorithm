
w,n = map(int,input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x:(-x[1]))

result = 0
for data in arr:
    if data[0] <= w:
        result += data[0] * data[1]
        w -= data[0]
    else:
        result +=  w * data[1]
        break

print(result)