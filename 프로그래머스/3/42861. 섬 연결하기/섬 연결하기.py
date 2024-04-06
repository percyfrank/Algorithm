def solution(n, costs):
    
    answer = 0
    costs.sort(key=lambda x:x[2])
    link = set([costs[0][0]])
    
    while len(link) < n:
        for start,end,cost in costs:
            if start in link and end in link:
                continue
            if start in link or end in link:
                link.update([start,end])
                answer += cost
                break
    
    return answer