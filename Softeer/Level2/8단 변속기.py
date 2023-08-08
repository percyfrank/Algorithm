import sys
input = sys.stdin.readline

arr = list(map(int,input().split()))

a_cnt, d_cnt = 0, 0
for i in range(7):
    if arr[i+1] == arr[i] + 1:
        a_cnt += 1
    elif arr[i+1] == arr[i] - 1:
        d_cnt += 1
    else:
        break

if a_cnt == 7:
    print("ascending")
elif d_cnt == 7:
    print("descending")
else:
    print("mixed")