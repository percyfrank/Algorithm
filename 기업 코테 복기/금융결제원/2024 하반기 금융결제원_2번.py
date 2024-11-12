

def find_possible_words(idx, word):
    global possible_s

    if idx == len(s):
        possible_s.append("".join(word))
        return

    if s[idx] == ' ':
        find_possible_words(idx + 1, word)
        find_possible_words(idx + 1, word + ' ')
    else:
        find_possible_words(idx + 1, word + s[idx])


s = input()
n = int(input())
words = [input() for _ in range(n)]
possible_s = []
s = s.lower()
find_possible_words(0, '')

answer = []
for word in words:
    word = word.lower()
    if word == s:
        answer.append(1)
    else:
        if word in possible_s:
            answer.append(1)
        else:
            answer.append(0)

print(answer)


#### 문제
# 문자열 s가 주어지고, 이어지는 문자열 집합을 대상으로 s와 일치하는지를 각각 구하라.
# 일치하는지를 확인하는 규칙은 3가지가 존재한다.
# 1. 문자열 s와 완전히 일치할 시 일치하는 것으로 본다.
# 2. s 내에 띄어쓰기를 생략했을 때 일치해도 두 문자열이 일치하는 것으로 본다.
# 3.대소문자 차이는 신경쓰지 않는다.
# 4. 이외의 모든 경우는 일치하지 않는 것으로 본다.(띄어쓰기를 잘못한 경우 등)
# s와 일치하면 1, 일치하지 않으면 0으로 표시.

#### 입력
# Nile River
# 7
# Nile River
# NileRiver
# Ni leRi ver
# River Nile
# Mississippi River
# nile rivER
# NILERIVER
#
#### 출력
# [1,1,0,0,0,1,1]

#### 입력
# A B C
# 6
# x y z
# A bc
# ab C
# aBc
# abcd
# A B C D
#
#### 출력
# [0,1,1,1,0,0]