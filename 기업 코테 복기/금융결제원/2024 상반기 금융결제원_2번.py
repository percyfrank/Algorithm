from itertools import product


keys = input()
t = int(input())
total = list(product([False, True], repeat=len(keys)))

answer = []
for times in total:
    tmp = []
    for idx, time in enumerate(times):
        if time:
            tmp.append([idx, idx])
        else:
            tmp.append([idx, idx+t+0.5])

    tmp.sort(key=lambda x: x[1])
    word = []
    for idx, time in tmp:
        if word and keys[idx] == '-':
            word.pop()  # ["0","AB","B"]
            # word.pop(0)   # ["0","A","AB","B"]
        elif keys[idx] != '-':
            word.append(keys[idx])

    word = "".join(word)
    print(word)
    if word == "":
        word = "0"
    if word not in answer:
        answer.append(word)

answer.sort()
print(answer)

#### 문제
# keys = 문자열 <= 15
# t = 시간
# 문자열 즉시 출력 or 지연(t+0.5) 출력 가능
# 각 문자마다 즉시 출력, 지연 출력 선택 횟수 제한 없음
# 가능한 모든 문자열 조합 정렬된 상태로 구하기
#### 문자열이 "-"인 경우 앞에서부터 문자열 1개 지우기 => 뒤에서부터 지우는 건지 불명확함
# 문자열 전체가 공백일 경우 "0"으로 대체 출력

#### 입출력
# | keys | t | result |
# | "BA" | 1 | ["AB","BA"] |
# | "YOLO" | 2 | ["LYOO","OLYO","OYLO","OYOL","YLOO","YOLO","YOOL"] |
# | "-A-B" | 1 | ["0","A","AB","B"] |
