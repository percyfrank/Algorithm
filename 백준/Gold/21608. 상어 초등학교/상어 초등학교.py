n = int(input())
students = [list(map(int, input().split())) for _ in range(n ** 2)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
seat = [[0] * n for _ in range(n)]

for i in range(n ** 2):
    student_num = students[i][0]
    student_like_list = students[i][1:]
    seat_position = []
    for x in range(n):
        for y in range(n):
            if seat[x][y] == 0:
                blank = 0
                like = 0
                for j in range(4):
                    nx = x + dx[j]
                    ny = y + dy[j]
                    if 0 <= nx < n and 0 <= ny < n:
                        if seat[nx][ny] in student_like_list:
                            like += 1
                        if seat[nx][ny] == 0:
                            blank += 1
                seat_position.append([like, blank, x, y])
    seat_position.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    seat[seat_position[0][2]][seat_position[0][3]] = student_num

students.sort(key=lambda x:(x[0]))
answer = 0
for x in range(n):
    for y in range(n):
        target = seat[x][y]
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if seat[nx][ny] in students[target-1][1:]:
                    cnt += 1
        if cnt == 1:
            answer += 1
        elif cnt == 2:
            answer += 10
        elif cnt == 3:
            answer += 100
        elif cnt == 4:
            answer += 1000

print(answer)