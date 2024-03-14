import heapq
import sys


def dijkstra(start):
    times = [float('inf')] * (N + 1)
    q = []
    heapq.heappush(q, (0, start))
    times[start] = 0

    while q:
        curr_time, curr_node = heapq.heappop(q)
        if times[curr_node] < curr_time:
            continue

        for next_node, next_time in graph[curr_node].items():
            if curr_time + next_time < times[next_node]:
                times[next_node] = curr_time + next_time
                heapq.heappush(q, (curr_time + next_time, next_node))

    return times


input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = [{} for _ in range(N + 1)]
for _ in range(M):
    u, v, time = map(int, input().split())
    graph[u][v] = time

tmp = dijkstra(X)
answer = 0
for i in range(1, N + 1):
    tmp[i] += dijkstra(i)[X]
    answer = max(answer, tmp[i])
print(answer)