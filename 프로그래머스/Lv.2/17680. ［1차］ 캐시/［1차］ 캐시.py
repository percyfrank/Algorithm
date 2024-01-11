from collections import deque

def solution(cacheSize, cities):
    
    q = deque(maxlen=cacheSize)
    answer = 0
    
    for city in cities:
        city = city.lower()
        if city not in q:            
            q.append(city)
            answer += 5
        else:
            q.remove(city)
            q.append(city)
            answer += 1
        
    return answer