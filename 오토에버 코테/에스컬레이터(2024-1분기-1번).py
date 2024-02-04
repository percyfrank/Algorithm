
import time
n = int(input())
escalator = [list(map(int, input().split(" "))) for _ in range(n)]

start_time = time.perf_counter()

dp = [[float('inf')] * 3 for _ in range(n)]
for i in range(len(escalator[0])):
    if escalator[0][i] == 0:
        dp[0][i] = abs(i-1)

for i in range(1,n):
    for j in range(3):
        if escalator[i][j] == 0:
            dp[i][j] = min(dp[i-1][0]+abs(j-0), dp[i-1][1]+abs(j-1), dp[i-1][2]+abs(j-2))

print(min(dp[n-1]))

end_time = time.perf_counter()
print(f"time elapsed : {int(round((end_time - start_time) * 1000))}ms")

# 에스컬레이터의 한 줄엔 3칸이 있다.
# 한 줄에 모든 사람이 서있는 경우는 없다.
# 0은 사람이 없는 칸이고, 1은 사람이 있는 칸이다.
# 줄의 수는 5이상 1000이하이다.
# 에스컬레이터의 맨 위에선 가운데 칸에서 시작한다.
# 옆으로 이동하면 칸을 이동하지 않는 것으로 한다.
# 에스컬레이터의 맨 아래까지 이동해야 하는 최소거리를 구하라.

# 입력
# 에스컬레이터 줄 수
# 에스컬레이터 정보

# 5
# 0 1 0
# 1 0 0
# 0 1 0
# 0 0 1
# 0 1 0
#
# 3
#
# 7
# 0 1 1
# 1 0 0
# 0 0 1
# 1 1 0
# 0 1 0
# 1 0 1
# 1 1 0
#
# 5

# 시간 초과 코드
# def dfs(row, col, cnt):
#     global ans
#     if row == n:
#         ans = min(ans, cnt)
#         return
#
#     for i in range(3):
#         if escalator[row][i] == 0 and not visited[row][i]:
#             visited[row][i] = True
#             dfs(row+1, i, cnt + abs(i-col))
#             visited[row][i] = False
#
#
# ans = float('inf')
# visited = [[False] * 3 for _ in range(n)]
# dfs(0, 1, 0)
# print(ans)