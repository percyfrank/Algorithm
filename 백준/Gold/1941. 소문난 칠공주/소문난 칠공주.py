from collections import deque

def check_adjacency(possible_seat):
    
    visited = [False] * 7
    q = deque()
    q.append(possible_seat[0])
    visited[0] = True
    cnt = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) in possible_seat:
                idx = possible_seat.index((nx, ny))
                if not visited[idx]:
                    visited[idx] = True
                    q.append((nx, ny))
                    cnt += 1
    if cnt != 7:
        return False
    return True

matrix = [input() for _ in range(5)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = 0
possible_seat = []
    
def backtracking(idx, yCnt):
    global ans
        
    if yCnt >= 4:
        return

    if len(possible_seat) == 7:
        if check_adjacency(possible_seat):
            ans += 1
        return
        
    for i in range(idx, 25):
        x = i // 5
        y = i % 5
        possible_seat.append((x, y))
        backtracking(i+1, yCnt + (matrix[x][y] == "Y"))
        possible_seat.pop()
        
backtracking(0, 0)
print(ans)