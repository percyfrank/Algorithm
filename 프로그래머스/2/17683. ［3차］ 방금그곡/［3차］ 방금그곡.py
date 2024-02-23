def solution(m, musicinfos):
    answer = []
    m = m.replace('A#','H').replace('C#','I').replace('D#','J').replace('E#','K').replace('F#','L').replace('G#','M').replace('B#','N')
    
    for musicinfo in musicinfos:
        start, end, title, melody = musicinfo.split(",")
        start = int(start[:2]) * 60 + int(start[3:])
        end = int(end[:2]) * 60 + int(end[3:])
        play_time = end-start
        
        melody = melody.replace('A#','H').replace('C#','I').replace('D#','J').replace('E#','K').replace('F#','L').replace('G#','M').replace('B#','N')

        if play_time <= len(melody):
            melody = melody[:play_time]
        else:
            q,r = divmod(play_time, len(melody))
            melody = melody * q + melody[:r]
        print(m, melody)
        
        # 음악 제목 찾기
        if melody.find(m) != -1:
            answer.append([title,play_time])            
    
    answer.sort(key=lambda x:(-x[1], x[0]))
    return answer[0][0] if answer else "(None)"