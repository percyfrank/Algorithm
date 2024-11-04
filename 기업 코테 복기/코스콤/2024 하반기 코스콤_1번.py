


n = int(input())
shifts = []
for i in range(n):
    shifts.append(input())
staff = int(input())

days = len(shifts[0])
answer = [staff] * days
flag = [True] * n           # 찬스 가능 여부
possibles = [[] for _ in range(days)]       # 날짜별 근무 가능일자
for i, shift in enumerate(shifts):
    for j in range(days):
        if shift[j] == "O" and answer[j] > 0:
            answer[j] -= 1
        elif shift[j] == "A":
            possibles[j].append(i)

for i,possible in enumerate(possibles):
    if possible:
        for j in range(len(possible)):
            if flag[possible[j]] and answer[i] > 0:
                answer[i] -= 1
                flag[possible[j]] = False

print(answer)

#### 문제
# shifts = 직원 근무표 리스트
# 2<= shifts의 길이 <= 100
# 1 <= shift[i]의 길이 <= 500
# staff = 하루에 필요한 직원 수
# "O" : 근무 희망
# "X" : 근무 불가
# "A" : 근무 가능
#
##### 조건
# 근무 희망일자를 먼저 배치한 후, 하루에 필요한 직원수보다 적을 경우엔
# 번호가 앞인 직원 순서대로 근무 가능일자에 배치할 수 있다.
# 이 때, 근무 가능일자 배치는 한 사람당 단 1번 가능하다.
# 근무 가능일자까지 배치하고 나서 추가적으로 필요한 직원의 수를 날짜 순서대로 구하기
#
#
##### 입력
# 4
# OAOOOOOO
# OXOXOXX
# OXOAOXX
# OOOAXXA
# 3
#
#### 출력
# [0,1,0,0,0,2,2]
#
#### 입력
# 3
# AO
# AX
# AA
# 2
#
##### 출력
# [0,0]