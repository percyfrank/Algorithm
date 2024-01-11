def solution(msg):
    
    dicts = {chr(65+i): i+1  for i in range(26)}
    answer = []
    w,c = 0,0
    
    while True:
        c += 1
        if c == len(msg):
            answer.append(dicts[msg[w:c]])
            break
        
        if msg[w:c+1] not in dicts.keys():
            answer.append(dicts[msg[w:c]])
            dicts[msg[w:c+1]] = len(dicts) + 1
            w = c
            
    return answer