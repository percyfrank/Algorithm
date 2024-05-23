

txs = list(map(int, input().split()))
n = int(input())

errors = []
for _ in range(n):
    error, duration = map(int, input().split())
    errors.append([error, error+duration])

times = []
start = 0
for tx in txs:
    end = start + tx
    times.append([start, end])
    start = end

visited = [True] * len(times)
for errorS, errorE in errors:
    for i, (s,e) in enumerate(times):
        if not visited[i]:
            continue
        if (errorS <= s <= errorE) and (errorS <= e <= errorE):
            visited[i] = False
        elif s <= errorS <= e and s <= errorE <= e:
            visited[i] = False
        elif errorS <= s < errorE:
            visited[i] = False
        elif errorS < e <= errorE:
            visited[i] = False


# for i, (s,e) in enumerate(times):
#     for errorS, errorE in errors:
#         if not visited[i]:
#             continue
#         if s <= errorS <= e and s <= errorE <= e:
#             visited[i] = False
#         elif (errorS <= s <= errorE) and (errorS <= e <= errorE):
#             visited[i] = False
#         elif s <= errorS < e:
#             visited[i] = False
#         elif s < errorE <= e:
#             visited[i] = False

print(visited)
answer = 0
for visit in visited:
    if visit:
        answer += 1

print(answer)

#### 문제
# txs = 작업 시간 리스트
# n = 작업 에러 횟수
# errors = 작업 에러(에러 시작시간,에러 지속시간)
# 정상적으로 작업을 마친 횟수 구하기


# # 입력
# 6 7 4 6 5 6
# 2
# 7 9
# 28 9
#
# # 출력
# 3
#
# # 입력
# 1 2 11 3 5 10 4 4 100
# 4
# 0 1
# 5 1
# 13 9
# 27 3
#
# # 출력
# 4
#
# # 입력
# 1 1
# 1
# 100000 1000
# 2
#
# # 출력
# 2





