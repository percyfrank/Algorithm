
n,m = map(int,input().split())

chart = []
for _ in range(n):
    arr = list(map(int,input().split()))
    tmp = []
    start = 0
    tmp.append(0)
    for i in range(len(arr)):
        tmp.append(start + arr[i])
        start += arr[i]
    chart.append(tmp)

for _ in range(m):
    x,y,X,Y = map(int,input().split())
    result = 0
    for i in range(x-1,X):
        result += chart[i][Y] - chart[i][y-1]
    print(result)


