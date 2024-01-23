def solution(record):
    
    answer = []
    name = {}
    order = {"Leave" : "님이 나갔습니다.","Enter":"님이 들어왔습니다."}
    for rc in record:
        tmp = rc.split(" ")
        if tmp[0] != "Leave":
            name[tmp[1]] = tmp[2]
    
    for rc in record:
        tmp = rc.split(" ")
        if tmp[0] != "Change":
            answer.append(name[tmp[1]]+order[tmp[0]])
    
    return answer