import sys
input = sys.stdin.readline

n, m = map(int, input().split())

sec_limit = [list(map(int, input().split())) for _ in range(n)]
test = [list(map(int, input().split())) for _ in range(m)]

speed_limit = []
for sector, limit in sec_limit:
    speed_limit += [limit for _ in range(sector)]

speed_test = []
for sector, t_limit in test:
    speed_test += [t_limit for _ in range(sector)]

MAX = 0
for i in range(100):
    MAX = max(MAX, speed_test[i]-speed_limit[i])

print(MAX)
