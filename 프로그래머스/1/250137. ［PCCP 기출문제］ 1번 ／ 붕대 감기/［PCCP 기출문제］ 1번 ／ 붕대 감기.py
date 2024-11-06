def solution(bandage, health, attacks):
    
    last_time = attacks[-1][0]
    idx, cnt = 0, 0    
    curr_time = 0
    curr_health = health
    while curr_time <= last_time:
        if curr_time == attacks[idx][0]:
            cnt = 0
            curr_health -= attacks[idx][1]
            if curr_health <= 0:
                curr_health = -1
                break
            curr_time += 1
            idx += 1
            continue
        
        cnt += 1
        curr_health += bandage[1]                    
        if cnt == bandage[0]:
            cnt = 0
            curr_health += bandage[2]            
        if curr_health > health:
            curr_health = health
                
        curr_time += 1
        
    return curr_health