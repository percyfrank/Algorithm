import heapq
import sys


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        for next_node, next_dist in graph[now].items():
            if dist + next_dist < distances[next_node]:
                distances[next_node] = dist + next_dist
                heapq.heappush(q, (dist + next_dist, next_node))


input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())

graph = [{} for _ in range(V + 1)]
for _ in range(E):
    u, v, cost = map(int, input().split())
    if v not in graph[u] or graph[u][v] > cost:
        graph[u][v] = cost

distances = [float('inf')] * (V + 1)

dijkstra(K)

for i in range(1, V+1):
    if distances[i] == float('inf'):
        print("INF")
    else:
        print(distances[i])
