n = int(input())

tmp = []
answer = []
num = 1

for _ in range(n):
    target = int(input())
    while num <= target:
        tmp.append(num)
        num += 1
        answer.append("+")
    if tmp[-1] == target:
        tmp.pop()
        answer.append("-")
    else:
        print("NO")
        answer = []
        break

if answer:
    for data in answer:
        print(data)