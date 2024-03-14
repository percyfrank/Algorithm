import heapq
import sys


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                prev_node[i[0]] = now
                heapq.heappush(q, (cost, i[0]))


input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
distances = [float('inf')] * (n + 1)

for _ in range(m):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))
start, end = map(int, input().split())

prev_node = [0] * (n + 1)
dijkstra(start)
print(distances[end])

paths = [end]
while True:
    if end == start:
        break
    end = prev_node[end]
    paths.append(end)

paths.reverse()
print(len(paths))
print(*paths)