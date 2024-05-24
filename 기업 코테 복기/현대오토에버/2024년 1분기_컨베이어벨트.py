

import time
from collections import deque

total = list(map(int, input().rstrip().split(" ")))
n = int(input())
lists = list(map(int, input().rstrip().split(" ")))

start_time = time.perf_counter()

lists = deque(lists)
ans = float('inf')
for _ in range(n):
    dic = {i+1 : total[i] for i in range(5)}
    cnt = 0
    for i in range(n):
        if list(dic.values()).count(0) == 5:
            break
        cnt += 1
        if dic[lists[i]] == 0:
            continue
        dic[lists[i]] -= 1
    ans = min(ans, cnt)
    lists.rotate(-1)

if ans != n:
    print(ans)
else:
    print(-1)

end_time = time.perf_counter()
print(f"time elapsed : {int(round((end_time - start_time) * 1000))}ms")


# 부품종류는 총 5가지
# 부품별 필요 갯수는 0개 이상 5개 이하
# 적어도 한 개의 부품을 필요로 한다.
# 컨베이어 벨트 위 부품 수 n은 1개 이상 100개 이하이다.
# 컨베이어 벨트 위를 지나면서 필요한 부품을 다 얻기 위한 최소 부품 확인 갯수를 구하라.
# 컨베이어 벨트의 특정 지점에서 부터 확인을 시작할 수 있고, 컨베이어 벨트는 원형으로 되어있다.
# 컨베이어 벨트는 시계반대방향으로 움직인다.
# 입력값의 컨베이어 부품 수는 시계방향순으로 인력받는다.

# 입력
# 부품수
# 컨베이어벨트 위 부품 갯수
# 컨베이어벨트 위 부품 정보

# 1 1 0 0 2
# 9
# 5 1 1 3 3 2 1 5 1
#
# 5
#
# 1 1 1 1 0
# 12
# 1 2 3 2 5 1 2 1 4 4 1 1
#
# 6
#
# 4 0 2 0 0
# 7
# 2 1 1 1 3 1 5
#
# -1


