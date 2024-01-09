def solution(s):
    
    binCnt, cnt = 0,0
    while True:
        
        if s == "1":
            break
        
        tmp = len(s) - s.count("0")
        cnt += s.count("0")
        s = bin(tmp)[2:]
        binCnt += 1
        
    return [binCnt,cnt]