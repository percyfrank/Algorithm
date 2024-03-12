import heapq

def solution(N, road, K):
    
    def dijkstra(start):

        q = []
        heapq.heappush(q, (0,start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for i in maps[now]:
                if dist+i[1] < distance[i[0]]:
                    distance[i[0]] = dist + i[1]
                    heapq.heappush(q,(dist+i[1],i[0]))

    distance = [float('inf')] * (N+1)         
    maps = [[] for _ in range(N+1)]
    for a,b,cost in road:
        maps[a].append((b,cost))
        maps[b].append((a,cost))
    
    dijkstra(1)
    
    answer = 0
    for i in range(1,N+1):
        if distance[i] <= K:
            answer += 1
            
    return answer