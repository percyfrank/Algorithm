from math import ceil

def solution(progresses, speeds):    

    release = []
    for progress,speed in zip(progresses,speeds):
        progress = 100 - progress
        release.append(ceil(progress / speed))
    
    answer = []
    tmp = []
    for data in release:
        if len(tmp) == 0:
            tmp.append(data)
            continue
        if tmp[0] >= data:
            tmp.append(data)
        else:
            answer.append(len(tmp))
            tmp.clear()
            tmp.append(data)
    answer.append(len(tmp))
    
    return answer