n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    flag = True
    target = word[0]
    for i in range(1,len(word)):
        if word[i] in target:
            target += word[i]
        else:
            for j in range(i):
                if word[i] in word[:j]:
                    flag = False
                    break
            target = word[i]
    if flag:
        cnt += 1
print(cnt)