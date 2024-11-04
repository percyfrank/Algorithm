

def getNumberOfCase(arr):
    a = 12 * 11 * 10 * 9 * 8
    b = 12 * 11 * 10 * 9
    c = 12 * 11 * 10
    d = 12 * 11
    e = 12 ** 5

    if arr == [1, 1, 1, 1, 1]:
        return a
    elif arr == [1, 1, 1, 2]:
        return a + b
    elif arr == [1, 1, 3]:
        return a + 3 * b + c
    elif arr == [1, 4]:
        return a + 6 * b + 4 * c + d
    elif arr == [1, 2, 2]:
        return a + 2 * b + c
    elif arr == [2, 3]:
        return a + 4 * b + 3 * c + d
    elif arr == [5]:
        return e

crops = []
for i in range(5):
    crops.append(list(input()))

crops_intersect = [[i] for i in range(5)]

for i in range(5):
    for j in range(i + 1, 5):
        intersect = set(crops[i]).intersection(set(crops[j]))
        # print(intersect)
        if len(intersect) >= 2:
            crops_intersect[i].append(j)
            crops_intersect[j].append(i)

# print(crops_intersect)

res = []
for crop_combine in crops_intersect:
    crop_combine = sorted(crop_combine)
    if crop_combine not in res:
        res.append(crop_combine)

# print(res)

cnt = []
for pairs in res:
    cnt.append(len(pairs))
cnt.sort()

print(getNumberOfCase(cnt))


#### 문제
# 5개의 농가가 각각 3개의 작물을 12개의 밭에서 재배하려고 한다.
# 밭 한 곳에 여러 농가가 작물을 재배하려면 농가 간에 작물 2개 이상이 겹쳐야만 가능하다.
# 농가 5 곳의 작물이 각각 주어질 때, 재배할 수 있는 서로 다른 경우의 수를 구하라.
#
#
#### 입력
# ABC
# CDE
# EFG
# GHI
# IJK
#
#### 출력
# 95040
#
#
#### 입력
# ABC
# ABC
# DEF
# GHI
# IJK
#
#### 출력
# 106920
#
#### 입력
# ABC
# ABC
# ABC
# DEF
# GHI
#
#### 출력
# 132000
#
#### 입력
# ABC
# ABC
# ABC
# ABC
# DEF
#
#### 출력
# 171732
#
#### 입력
# ABC
# ABC
# ABC
# ABC
# ABC
#
#### 출력
# 248832
#
#### 입력
# ABC
# ABC
# DEF
# DEF
# GHI
#
#### 출력
# 120120
#
#### 입력
# ABC
# ABC
# DEF
# DEF
# DEF
#
#### 출력
# 146652
