import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

tmp1 = []
result = float('inf')

def solve(idx):
    global result
    if len(tmp1) == n//2:
        tmp2 = []
        start = 0
        link = 0
        for i in range(n):
            if i not in tmp1:
                tmp2.append(i)
        for i in range(n//2-1):
            for j in range(i+1,n//2):
                start += arr[tmp1[i]][tmp1[j]] + arr[tmp1[j]][tmp1[i]]
                link += arr[tmp2[i]][tmp2[j]] + arr[tmp2[j]][tmp2[i]]
        result = min(result, abs(start-link))
        return

    for i in range(idx,n):
        if i not in tmp1:
            tmp1.append(i)
            solve(i+1)
            tmp1.pop()

solve(0)
print(result)