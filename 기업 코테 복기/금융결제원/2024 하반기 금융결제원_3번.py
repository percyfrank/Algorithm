from collections import defaultdict

n = int(input())
nums = [input() for _ in range(n)]
nums_arr = []

for i, num in enumerate(nums):
    cnt = 1
    tmp = []
    for j in range(len(num) - 1):
        if num[j] == '0' and num[j+1] == '0':
            cnt = 0
        elif num[j] == '0' and num[j+1] == '1':
            cnt = 0
            cnt += 1
        elif num[j] == '1' and num[j+1] == '0':
            tmp.append(cnt)
            cnt = 0
        elif num[j] == '1' and num[j+1] == '1':
            cnt += 1
    if cnt != 0:
        tmp.append(cnt)
    nums_arr.append(tmp)

dic = defaultdict(list)
for i, arr in enumerate(nums_arr):
    dic[tuple(arr)].append(str(i + 1))

answer = []
for key, value in dic.items():
    if len(value) >= 2:
        answer.append(" ".join(value))

print(answer)


#### 문제
# 0과 1로 이루어진 문자열이 주어질 때, 연속하는 1의 갯수를 반환하는 배열을 만든다.
# 그 후, 그 배열들끼리 일치하는 문자열을 유사한 배열이라고 한다.
# 예를 들어, '011010111'의 경우 연속하는 1의 갯수가 2개, 1개, 3개이므로 배열은 [2, 1, 3]이다.
# 주어진 문자열들 중 유사한 배열 번호들을 묶어서 반환하라.

#### 입력
# 6
# 011010111
# 100110101
# 110100111
# 011011111
# 101100101
# 101101010
#
#### 출력
# ['1 3','2 5 6']