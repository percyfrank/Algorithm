
n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

result = float('inf')
tmp = []
visited = [False] * n

def solve():
    global result
    if len(tmp) == n//2:
        start = 0
        link = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += arr[i][j]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]
        result = min(result,abs(start-link))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            tmp.append(i)
            solve()
            tmp.pop()
            visited[i] = False

solve()
print(result)
