import sys
input = sys.stdin.readline

n = int(input())

start = 2
result = []

for _ in range(15):
    tmp = start + (start-1)
    result.append(tmp)
    start = tmp

print(result[n-1]**2)