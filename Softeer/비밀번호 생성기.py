

n = int(input())                                         # 사용자 수
arr = [list(map(int,input().split())) for _ in range(n)] # 비밀번호 생성기 정보
q = int(input())                                         # 인증시도

# U,T,X
for _ in range(q):
    idx, X, Y = map(int,input().split())
    idx -= 1
    flag = False
    for v in range(X-3, X+4):
        if v < 0:
            continue
        cnt = arr[idx][0] * X * X
        cnt += arr[idx][1] * X
        cnt += arr[idx][2]
        cnt %= 999983
        if cnt == Y:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")