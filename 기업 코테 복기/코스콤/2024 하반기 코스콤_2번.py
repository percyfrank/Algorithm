

def dfs(idx, code):
    global possible_code

    if len(code) == k:
        possible_code.append("".join(code))
        return

    for i in range(idx, len(city)):
        if not visited[i] and len(code) < k:
            visited[i] = True
            code.append(city[i])
            dfs(i+1, code)
            visited[i] = False
            code.pop()


n = int(input())
cities = []
for _ in range(n):
    cities.append(input())

k = 1
region_codeList = []
while len(region_codeList) < n:
    region_codeList = []
    for i in range(n):
        city = cities[i]
        city_length = len(city)
        if city_length < k:
            city += "_" * (k - city_length)
        region_tmpCode = city[:k]
        if region_tmpCode not in region_codeList:
            region_codeList.append(region_tmpCode)
        else:
            visited = [False] * city_length
            flag = True
            possible_code = []
            dfs(0, [])
            possible_code.sort()
            for code in possible_code:
                if code not in region_codeList:
                    region_codeList.append(code)
                    flag = False
                    break

            if flag:
                k += 1
                break

print(region_codeList)

#### 문제
# 도시 이름으로 이루어진 배열(cities)이 주어진다.
# 도시 이름의 길이가 각기 다른 관계로 통일된 길이의 지역코드를 도시마다 부여하고자 한다.
# 이 때, 통일된 길이는 가장 짧게 정하도록 한다.
#
# 통일된 길이를 k라고 할 때, 지역코드 부여기준은 다음과 같다.
# 우선, 배열 순서대로 도시 이름의 앞 k자리를 떼어내 지역코드로 정한다.
# 만약, 자신의 순서 이전까지의 도시 지역코드와 겹친다면, 새로운 지역코드를 정해야한다.
# 순서가 바뀌지 않게 하면서 도시 이름의 k개 철자들로 이루어진 코드들을 만든 뒤,
# 사전 순으로 가장 앞에 오는 철자를 새로운 지역코드로 정한다.
#
# 단, 도시이름이 k보다 짧다면 "_"를 이어붙여서 지역코드를 부여해야 한다.
#
# 가장 짧은 지역코드 배열을 구하시오.


#### 조건
# 2 <= cities의 길이 <= 1000
# 도시 이름 <= 8

#### 입력
# ABC
# SEOUL
# BUSAN
# DAEGU
# DAEJEON
#
#### 출력
# [A, S, B, D ,E]
#
#### 입력
# DAE
# DAEGU
# DAEJEON
# DE
#
#### 출력
# [DA, AE, AJ, DE]
#
#### 입력
# DAEGU
# DAEJEON
# DAE
# DE
#
#### 출력
# [DAEG, DAEJ, DAE_, DE__]
#
#### 입력
# AAA
# AAAA
# AAAB
#
#### 출력
# [AAA_, AAAA, AAAB]
#
#### 입력
# X
# XX
# XXX
# XXXXX
# A
# AA
# AAA
# AAAAA
#
#### 출력
# [X____, XX__, XXX_, XXXX, A___, AA__, AAA_, AAAA]
