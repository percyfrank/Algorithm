from collections import defaultdict

n = int(input())
words = [input() for _ in range(n)]
dic = defaultdict(int)
for word in words:
    dic[word[0]] += 1

dic = dict(sorted(dic.items(), key=lambda x:x[0]))
ans = ""
for key,value in dic.items():
    if value >= 5:
        ans += key

print(ans) if len(ans) != 0 else print("PREDAJA")