import sys

input = sys.stdin.readline
n = int(input())

arr = set()
for _ in range(n):
    word = input()
    arr.add(word)
arr = list(arr)

arr.sort(key=lambda x : (len(x),x))

for data in arr:
    print(data, end ='')