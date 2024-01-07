from math import ceil

def solution(progresses, speeds):    

    release = []
    for progress,speed in zip(progresses,speeds):
        progress = 100 - progress
        release.append(ceil(progress / speed))
    
    answer = []
    prev = release[0]
    cnt = 0
    for i in range(len(release)):
        if prev < release[i]:
            answer.append(cnt)
            prev = release[i]
            cnt = 0
        cnt += 1
    answer.append(cnt)
    
    return answer