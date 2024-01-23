def solution(record):
    
    answer = []
    name = {}
    for rc in record:
        tmp = rc.split(" ")
        if tmp[0] == "Leave":
            answer.append([tmp[1],"Leave"])
        else:
            command,id,nickname = tmp[0],tmp[1],tmp[2]
            if command == "Enter":
                answer.append([id,"Enter"])
                name[id] = nickname
            elif command == "Change":
                name[id] = nickname
    
    order = {"Leave" : "님이 나갔습니다.","Enter":"님이 들어왔습니다."}
    result = []
    for id, comm in answer:
        if id in name.keys():
            result.append(name[id]+order[comm])
    
    return result