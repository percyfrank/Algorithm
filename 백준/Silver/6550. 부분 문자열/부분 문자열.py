import sys

while True:
    word = sys.stdin.readline().rstrip()
    if word == '':
        break
    s,t = word.split()
    idx = 0
    for i in range(len(t)):
        if s[idx] == t[i]:
            idx += 1
        if idx == len(s):
            break
    print("No") if idx < len(s) else print("Yes")