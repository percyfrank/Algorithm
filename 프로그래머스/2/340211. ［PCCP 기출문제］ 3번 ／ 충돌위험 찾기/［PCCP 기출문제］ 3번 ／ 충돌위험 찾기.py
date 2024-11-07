from collections import Counter

def solution(points, routes):

    answer = 0    
    robot_total_cnt = len(routes)
    max_move_cnt = 0
    routes_detail = [[] for _ in range(robot_total_cnt)]
    
    for i in range(robot_total_cnt):
        for j in range(len(routes[i])-1):
            x,y = points[routes[i][j]-1]
            nx,ny = points[routes[i][j+1]-1]
            dx,dy = nx-x,ny-y
            
            if j == 0:
                routes_detail[i].append((x,y))
            
            while dx != 0:
                if dx > 0:
                    x += 1
                    dx -= 1
                else:
                    x -= 1
                    dx += 1
                routes_detail[i].append((x,y))
            
            while dy != 0:
                if dy > 0:
                    y += 1
                    dy -= 1
                else:
                    y -= 1
                    dy += 1
                routes_detail[i].append((x,y))
                
        max_move_cnt = max(max_move_cnt,len(routes_detail[i]))
    
    for i in range(max_move_cnt):
        collides = []
        for j in range(robot_total_cnt):
            if len(routes_detail[j]) <= i:
                continue
            collides.append(routes_detail[j][i])
        
        collides = Counter(collides)
        for collide in collides.values():
            if collide >= 2:
                answer += 1
                continue
    
    return answer