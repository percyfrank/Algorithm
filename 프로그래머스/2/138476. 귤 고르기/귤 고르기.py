def solution(k, tangerine):
    
    tmp = dict()
    for tan in tangerine:
        tmp.setdefault(tan,0)
        tmp[tan] += 1
        
    answer, cnt = 0,0
    tmp = dict(sorted(tmp.items(), key=lambda x:x[1], reverse=True))
    for key,value in tmp.items():
        cnt += value
        answer += 1
        if cnt >= k:
            break

    return answer