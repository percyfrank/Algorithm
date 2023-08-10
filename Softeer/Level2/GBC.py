import sys
input = sys.stdin.readline

n,m = map(int,input().split())

start = 1
total = [0] * 101
for _ in range(n):
    sector, limit = map(int, input().split())
    for i in range(start, start+sector):
        total[i] = limit
    start += sector

s_start = 1
MAX = 0
for _ in range(m):
    sec, speed = map(int, input().split())
    for i in range(s_start, s_start+sec):
        MAX = max(MAX, speed-total[i])
    s_start += sec

print(MAX)
