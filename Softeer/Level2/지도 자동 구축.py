import sys
input = sys.stdin.readline

n = int(input())

result = [0] * 16
result[0] = 2

for i in range(1,n+1):
    result[i] = result[i-1] + (result[i-1] - 1)

print(result[n]**2)