

n = int(input())
answer = 0
for _ in range(n):
    word = input()
    word = word.lower()
    flag = False
    for i in range(len(word)-1):
        if word[i:i+2] == "nh":
            flag = True
            break
    if not flag:
        answer += 500

print(answer)


#### 문제
# 대소문자를 구분하지 않고, 문자열이 "nh"를 포함하지 않으면 타행이체 수수료를 낸다.
# 주어진 문자열 배열의 수수료를 구하라.
#
#### 조건
# 2 <= 문자열 배열 길이 <= 100
# 문자열 하나의 길이 <= 20
#
#### 입력
# NH
# nH
# NH_bank
# ABCnhDEF
# ABC
# NongHyup
# N_H
#
#### 출력
# 1500
#
#### 입력
# abcN_Hdef
# HN
# ABC_nh
# nH_ABC
# xyzNh
# nhxyz
# n_h
# nah
#
#### 출력
# 20000