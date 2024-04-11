n = int(input())
arr = set(map(int,input().split()))
m = int(input())
cards = list(map(int,input().split()))

for card in cards:
    if card in arr:
        print(1,end=" ")
    else:
        print(0,end=" ")