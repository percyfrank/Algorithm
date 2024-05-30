
import sys

input = sys.stdin.readline

position = input().rstrip().replace('()', 'l')

bar = []
answer = 0
for p in position:
    if bar and p == 'l':
        answer += len(bar)
    elif p == '(':
        bar.append(p)
    elif bar and p == ')':
        bar.pop()
        answer += 1

print(answer)