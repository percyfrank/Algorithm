def solution(routes):
    
    routes.sort(key=lambda x:x[1])
    camera = -30001
    answer = 0
    
    for route in routes:
        if route[0] > camera:
            answer += 1
            camera = route[1]

    return answer