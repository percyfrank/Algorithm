
n = int(input())
num = list(map(int,input().split()))
cal = list(map(int,input().split()))

MAX = -float('inf')
MIN = float('inf')

def solve(result, idx):
    global MAX, MIN
    if idx == n:
        MAX = max(MAX,result)
        MIN = min(MIN,result)
        return
    for i in range(4):
        tmp = result
        if cal[i]:
            if i == 0:
                result += num[idx]
            elif i == 1:
                result -= num[idx]
            elif i == 2:
                result *= num[idx]
            else:
                result = int(result/num[idx])

            cal[i] -= 1
            solve(result,idx+1)
            result = tmp
            cal[i] += 1

solve(num[0],1)
print(MAX)
print(MIN)

