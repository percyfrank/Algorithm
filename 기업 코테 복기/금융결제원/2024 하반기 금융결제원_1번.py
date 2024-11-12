

n = int(input())
task_arr = [int(input()) for _ in range(n)]
t = int(input())
e = int(input())

answer = []
for i in range(1, e + 1):
    cnt = 0
    for j in range(len(task_arr)):
        a, b = divmod(task_arr[j], 10000)
        if a == t:
            my_task = b % t
            if my_task == 0 and i == e:
                cnt += 1
                continue
            if my_task == i:
                cnt += 1
    if cnt > 0:
        answer.append((i, cnt))

answer.sort(key=lambda x: (-x[1], x[0]))
print(answer[0][0])

#### 문제
# 업무코드 5자리는 앞 1자리의 업무 분류코드와 이후 4자리의 업무번호로 이루어진다.
# 이 때, 1 ~ e번으로 이루어진 직원들이 존재한다.
# 업무번호를 t로 나누었을 때의 나머지가 자신의 번호와 일치한다면 그 업무코드는 해당 직원이 담당하는 업무가 된다.
# 단, 나머지가 0인 경우 e번 직원이 담당한다.
# n개의 업무코드가 주어질 때, 업무 분류코드가 t인 업무들을 가장 많이 담당하는 직원의 번호를 구하라.
# 단, 업무를 가장 많이 담당하는 직원이 여러 명일 경우, 번호가 가장 작은 직원의 번호를 구한다.

#### 입력
# 7
# 10032
# 30052
# 50032
# 50052
# 50049
# 50072
# 50039
# 5
# 13

#### 출력
# 2