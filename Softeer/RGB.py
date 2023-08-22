from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

ans = -1

pos = [[] for _ in range(3)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == "R":
            pos[0].append((i, j))
        if arr[i][j] == "G":
            pos[1].append((i, j))
        if arr[i][j] == "B":
            pos[2].append((i, j))
        if arr[i][j] != "#":
            arr[i][j] = "."

print(pos)
print(arr)

def bfs(ex, ey):
    visit = [[-1 for _ in range(m)] for _ in range(n)]
    visit[0][0] = 0
    q = deque()
    q.append((0,0))

    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == -1 and arr[nx][ny] == '.':
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))

    return visit[ex][ey]

# idx는 RGB 중 어떤 것을 이동시킬 것인가
# len은 지금까지 이동한 거리의 총 합
def backtracking(idx, len):
    global ans

    if idx == 3:
        if ans == -1:
            ans = len
        ans = min(ans, len)
        return

    for px, py in pos[idx]: # px, py : 이번에 이동시키고 싶은 위치
        print(px,py)
        dist = bfs(px, py)   # 최단 거리 계산
        if dist == -1:
            continue
        arr[px][py] = '#'
        backtracking(idx+1, len+dist)
        arr[px][py] = '.'

backtracking(0,0)
print(ans)