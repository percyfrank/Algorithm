import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(start, target, chess, l):

    q = deque()
    q.append(start)
    chess[start[0]][start[1]] = 1

    while q:
        x, y = q.popleft()
        if (x, y) == target:
            return chess[x][y]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if not chess[nx][ny]:
                    chess[nx][ny] = chess[x][y] + 1
                    q.append((nx, ny))


def main():
    t = int(input())
    for _ in range(t):
        l = int(input())
        chess = [[0] * l for _ in range(l)]
        start = tuple(map(int, input().split()))
        target = tuple(map(int, input().split()))
        cnt = bfs(start, target, chess, l)
        print(cnt - 1)


if __name__ == "__main__":
    main()