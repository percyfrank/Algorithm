

n = int(input())
names = input().split()
m = int(input())
# n명 인원의 요일(5개), 시간(24), 분(10분 단위 6개)
mems = [[[[0 for _ in range(6)] for _ in range(24)] for _ in range(5)] for _ in range(n)]
conv_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

for _ in range(m):
    day, h1, m1, h2, m2, v = input().split() # day 요일에, h1:m1 부터 h2:m2 까지 v에 있는 인원이 같이 미팅을 한다.
    h1, m1, h2, m2 = int(h1), int(m1), int(h2), int(m2)
    day = conv_days.index(day)

    for x in v.split(','):
        idx = names.index(x)

        h, m = h1, m1
        while (h, m) != (h2, m2):
            mems[idx][day][h][m // 10] = 1 # 누구(idx)의 어떤 요일에 어떤 시간에 미팅을 하고 있다고 기록
            m += 10
            if m == 60:
                h += 1
                m = 0

q = int(input())
for _ in range(q):
    days, v = input().split() # 무슨 요일(days)에 어떤 인원(v)이 전부 포함된 미팅을 계획했는가
    days = days.split(',')
    v = [names.index(x) for x in v.split(',')]
    ans, cnt = 0, 0

    for _day in days: # 주어진 요일 모두를 탐색하며 최대를 탐색
        day = conv_days.index(_day)
        cnt = 0
        for h in range(9, 18): # 해당 요일(_day)에 9-18시까지 모든 사람이 빈 시간이면 cnt +10
            for m in range(0, 6):
                if all(mems[idx][day][h][m] == 0 for idx in v):
                    cnt += 10
                else:
                    cnt = 0
                ans = max(ans, cnt)
    print(ans)



'''
입력 예시

3
a b c
8
Mon 10 0 11 0 a,b,c
Tue 10 0 11 0 a,c,b
Wed 10 0 11 0 a,b,c
Thu 10 0 11 0 a,b,c
Fri 10 0 11 0 a,b,c
Mon 14 0 17 10 a,b
Tue 13 0 14 0 b,c
Wed 15 0 16 30 c,a

1
Mon,Tue,Wed a,b

'''