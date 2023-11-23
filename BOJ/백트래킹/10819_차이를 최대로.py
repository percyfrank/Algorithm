

n = int(input())
arr = list(map(int, input().split()))
visited = [False] * n
tmp = []
MAX = 0

def backtracking():
    global MAX
    SUM = 0
    if len(tmp) == n:
        for i in range(n-1):
            SUM += abs(tmp[i]-tmp[i+1])
        MAX = max(MAX, SUM)
        return

    for i in range(n):
        if not visited[i]:
            tmp.append(arr[i])
            visited[i] = True
            backtracking()
            tmp.pop()
            visited[i] = False

backtracking()
print(MAX)




