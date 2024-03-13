import heapq

def solution(N, road, K):
    
    def dijkstra(start):
        
        q = []
        heapq.heappush(q,(start,0))
        distance[start] = 0
        
        while q:
            now, dist = heapq.heappop(q)
                
            for next, cost in maps[now].items():
                if dist + cost < distance[next]:
                    distance[next] = dist + cost
                    heapq.heappush(q,(next,dist+cost))
    
    distance = [float('inf')] * (N+1)
    maps = [{} for _ in range(N+1)]
    for a,b,cost in road:
        if b not in maps[a] or cost < maps[a][b]:
            maps[a][b] = cost
            maps[b][a] = cost
    
    dijkstra(1)
    
    return len([i for i in range(1,N+1) if distance[i] <= K])