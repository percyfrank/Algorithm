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
        for next, next_dist in graph[now].items():
            if dist + next_dist < distances[next]:
                distances[next] = dist + next_dist
                prev_node[next] = now
                heapq.heappush(q, (dist + next_dist, next))

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [{} for _ in range(n + 1)]
for _ in range(m):
    u, v, cost = map(int, input().split())
    if v not in graph[u] or graph[u][v] > cost:
        graph[u][v] = cost
start, end = map(int, input().split())

distances = [float('inf')] * (n + 1)
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