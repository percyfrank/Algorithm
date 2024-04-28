def solution(bandage, health, attacks):

    # 공격 마지막 시간, 붕대감기 연속 시간
    curr = health
    end_time, heal_time, attackIdx = attacks[len(attacks)-1][0], 0, 0

    for curr_time in range(1,end_time+1):
        # 공격받은 경우
        if curr_time == attacks[attackIdx][0]:
            heal_time = 0
            curr -= attacks[attackIdx][1]
            attackIdx += 1
            if curr <= 0:
                return -1
        # 공격받지 않은 경우
        else:
            heal_time += 1
            curr += bandage[1]
            if heal_time == bandage[0]:
                curr += bandage[2]
                heal_time = 0
            if curr > health:
                curr = health
                
    return curr