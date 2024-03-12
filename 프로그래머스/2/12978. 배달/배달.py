def solution(N, road, K):

    def get_smallest_node():
        min_val = float('inf')
        idx = 0
        for i in range(1,N+1):
            if distance[i] < min_val and not visited[i]:
                min_val = distance[i]
                idx = i
        return idx
    
    def dijkstra(start):
        distance[start] = 0
        visited[start] = True
        
        for k,v in maps[start].items():
            distance[k] = v
            
        for i in range(N-1):
            now = get_smallest_node()
            visited[now] = True
            
            for node,dist in maps[now].items():
                if distance[now] + dist < distance[node]:
                    distance[node] = distance[now] + dist
                            
    visited = [False] * (N+1)
    distance = [float('inf')] * (N+1)            
    maps = [{} for _ in range(N+1)]
    for a,b,cost in road:
        if b not in maps[a] or maps[a][b] > cost:
            maps[a][b] = cost
            maps[b][a] = cost
            
    dijkstra(1)
    
    answer = 0
    for i in range(1,N+1):
        if distance[i] <= K:
            answer += 1
            
    return answer