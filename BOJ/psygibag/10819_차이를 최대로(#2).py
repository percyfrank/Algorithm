
n = int(input())
arr = list(map(int,input().split()))

result = []
visited = [False] * n
MAX = 0

def solve():
    global MAX
    tmp = 0
    if len(result) == n:
        for i in range(n-1):
            tmp += abs(result[i] - result[i+1])
        MAX = max(tmp,MAX)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            result.append(arr[i])
            solve()
            result.pop()
            visited[i] = False

solve()
print(MAX)