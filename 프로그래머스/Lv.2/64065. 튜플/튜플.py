def solution(s):
    
    s = s[2:-2].split("},{")
    s.sort(key=lambda x:len(x))
    
    answer = []
    for data in s:
        for num in list(map(int,data.split(","))):
            if num not in answer:
                answer.append(num)

    return answer