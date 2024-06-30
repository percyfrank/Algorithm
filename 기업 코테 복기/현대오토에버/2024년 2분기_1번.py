

from bisect import bisect_left, bisect_right

n, q, k = tuple(map(int, input().split()))
machine = list(map(int, input().split()))
cnt = [0] * n

for _ in range(q):
    s, e = tuple(map(int, input().split()))
    sIdx = bisect_left(machine, s)
    eIdx = bisect_right(machine, e)

    cnt[sIdx] += 1
    if eIdx < n:
        cnt[eIdx] -= 1

for i in range(1, n):
    cnt[i] += cnt[i-1]

for idx, c in enumerate(cnt):
    cnt[idx] = [idx, c]

cnt.sort(key=lambda x : (-x[1], x[0]))
print(machine[cnt[k][0]])

# 각 제품의 시작, 끝 설비 정보를 바탕으로 주어진 주요 설비 사용 횟수 중에
# 처분할 설비의 수를 제외한 설비 중에서 가장 많이 사용된 주요 설비 번호 출력
# 만약 설비를 처분하고 나서 가장 많이 사용된 주요 설비 횟수가 동일한 것이 여러 개라면
# 설비번호가 작은 것을 출력.

# 입력조건
# 0 <= K < N < 500,000
# 1 <= Q <= 500,000
# 1 <= 주요 설비 번호 <= 10^9
# 각 제품의 시작 설비, 끝 설비 정보 : 1 <= s < e <= 10^9


# 주요 설비 수(N), 제품 수(Q), 처분 설비 수(K)
# 6 5 2

# 주요 설비 수 리스트
# 3 7 10 13 17 20

# 각 제품의 시작 설비, 끝 설비 정보
# 1 10
# 3 9
# 4 23
# 12 19
# 3 15