
def dfs(idx, arr):
    if len(arr) == len(keys):
        if arr not in total:
            total.append(arr)
        return
    dfs(idx+1, arr+[False])
    dfs(idx+1, arr+[True])


keys = input()
t = int(input())
total = []
dfs(0, [])

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
        if word and keys[idx] == "-":
            word.pop()
        elif keys[idx] != "-":
            word.append(keys[idx])

    word = "".join(word)
    if word == "":
        word = "0"
    if word not in answer:
        answer.append(word)

answer.sort()
print(answer)


#### 문제
# keys = 문자열
# t = 시간
# 문자열을 즉시 출력하거나 지연(t+0.5) 출력 가능
# 즉시 출력 지연 출력은 언제든지 가능
# 가능한 문자열 조합 정렬해서 모두 구하기
# 문자열이 "-"인 경우 앞에서부터 문자열 1개 지우기
# 문자열이 공백일 경우 "0" 출력

# 입력
# | keys | t | result |
# | --- | --- | --- |
# | "BA" | 1 | ["AB","BA"] |
# | "YOLO" | 2 | ["LYOO","OLYO","OYLO","OYOL","YLOO","YOLO","YOOL"] |
# | "-A-B" | 1 | ["0","A","AB","B"] |