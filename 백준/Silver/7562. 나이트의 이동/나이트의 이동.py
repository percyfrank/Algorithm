import sys
from collections import deque

input = sys.stdin.readline

dirs = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

def bfs(start, target, chess, l):

    cnt = 0
    q = deque()
    q.append((start[0], start[1], cnt))
    chess[start[0]][start[1]] = 1

    while q:
        x, y, cnt = q.popleft()
        if (x, y) == target:
            return cnt
        for (dx, dy) in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < l and 0 <= ny < l:
                if not chess[nx][ny]:
                    chess[nx][ny] = 1
                    q.append((nx, ny, cnt+1))


def main():
    t = int(input())
    for _ in range(t):
        l = int(input())
        chess = [[0] * l for _ in range(l)]
        start = tuple(map(int, input().split()))
        target = tuple(map(int, input().split()))
        cnt = bfs(start, target, chess, l)
        print(cnt)


if __name__ == "__main__":
    main()