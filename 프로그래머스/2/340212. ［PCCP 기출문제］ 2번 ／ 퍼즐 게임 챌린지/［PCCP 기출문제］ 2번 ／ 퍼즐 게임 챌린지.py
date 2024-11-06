def solution(diffs, times, limit):
    
    lo = 1
    hi = max(diffs)    
    while lo < hi:
        level = (lo + hi) // 2
            
        time_taken = times[0]
        prev_time = times[0]
        for idx,(diff,time) in enumerate(zip(diffs,times)):
            if idx == 0:
                continue
            
            if diff <= level:
                time_taken += time
            else:
                cnt = diff - level
                time_taken += cnt * (time + prev_time) + time
            prev_time = time
        
        if time_taken <= limit:
            hi = level
        else:
            lo =  level + 1
    
    return lo