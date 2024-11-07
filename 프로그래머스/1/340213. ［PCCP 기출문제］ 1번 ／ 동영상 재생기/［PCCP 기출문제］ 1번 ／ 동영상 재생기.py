def to_second(time):
    return int(time.split(":")[0])*60 + int(time.split(":")[1])

def solution(video_len, pos, op_start, op_end, commands):
    
    video_len = to_second(video_len)
    pos = to_second(pos)
    op_start = to_second(op_start)
    op_end = to_second(op_end)
    
    for command in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        if command == "next":
            pos += 10
            if pos > video_len:
                pos = video_len
        elif command == "prev":
            pos -= 10
            if pos < 0:
                pos = 0
    if op_start <= pos <= op_end:
        pos = op_end
    
    m,s = divmod(pos,60)
    answer = (2-len(str(m)))*"0"+ str(m) + ":" + (2-len(str(s)))*"0" + str(s)
    return answer