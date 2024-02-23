def solution(m, musicinfos):
    
    def convert(music):
        music = music.replace('C#', 'c')
        music = music.replace('D#', 'd')
        music = music.replace('F#', 'f')
        music = music.replace('G#', 'g')
        music = music.replace('A#', 'a')
        music = music.replace('B#', 'b')
        return music
    
    answer = []
    m = convert(m)
    
    for musicinfo in musicinfos:
        start, end, title, melody = musicinfo.split(",")
        start = int(start[:2]) * 60 + int(start[3:])
        end = int(end[:2]) * 60 + int(end[3:])
        play_time = end-start
        
        melody = convert(melody)

        if play_time <= len(melody):
            melody = melody[:play_time]
        else:
            q,r = divmod(play_time, len(melody))
            melody = melody * q + melody[:r]
        print(m, melody)
        
        # 음악 제목 찾기
        if m in melody:
            answer.append([title,play_time])            
    
    answer.sort(key=lambda x:(-x[1], x[0]))
    return answer[0][0] if answer else "(None)"