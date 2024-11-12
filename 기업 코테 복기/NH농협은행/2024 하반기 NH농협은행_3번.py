from collections import deque


def bfs(x, y, target):
    q = deque()
    q.append((x, y, target))
    visited[x][y] = 1
    tmp.add(target)

    while q:
        x, y, target = q.popleft()
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                new_target = blocks[nx][ny]
                if visited[nx][ny] == 0:
                    if new_target == target or ny == y:
                        q.append((nx, ny, new_target))
                        visited[nx][ny] = 1
                        tmp.add(new_target)


n, m = map(int, input().split())
blocks = [[0] * m for _ in range(n)]
start = 1
for i in range(n):
    input_blocks = list(map(int, input().split()))
    j = 0
    for block in input_blocks:
        for _ in range(block):
            blocks[i][j] = start
            j += 1
        start += 1

l = int(input())
points = [list(map(int, input().split())) for _ in range(l)]
dx, dy = [1, 0, 0], [0, 1, -1]
answer = []
for x, y in points:
    tmp = set(blocks[x])
    target = min(tmp) + y
    y = blocks[x].index(target)
    visited = [[0] * m for _ in range(n)]
    tmp = set()
    bfs(x, y, target)
    answer.append(len(tmp) - 1)
print(answer)


#### 문제
# 입력으로 주어지는 블럭의 위치를 바탕으로 해당 블럭을 떠받치는 블럭들의 총 갯수를 구하라.
# 입력 첫째 줄엔 총 블럭의 행 수와 열 수가 주어짐.
# 두번째 줄부터 행 수만큼 각 블럭의 갯수가 주어짐. ex) 1 2 4일 경우 1개짜리, 2개짜리, 4개짜리 블럭임을 뜻함.
# 다음 줄엔 구해야 할 블럭의 갯수가 주어짐.
# 다음 줄엔 해당 블럭의 (x,y) 위치가 갯수만큼 주어짐.
# 아래 입력을 기준으로 (0,1)은 첫째 줄의 2개짜리 블럭을 뜻함.


#### 입력
# 4 7
# 1 2 4
# 1 1 2 3
# 2 3 1 1
# 1 1 2 3
# 2
# 0 1
# 1 1
#### 출력
# [8,3]
#
#### 입력
# 3 5
# 5
# 2 1 2
# 5
# 2
# 2 0
# 0 0
#### 출력
# [0,4]