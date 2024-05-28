from collections import deque

n = int(input())
cards = [i for i in range(1,n+1)]
cards = deque(cards)

while True:
    if len(cards) == 1:
        print(*cards)
        break
    cards.popleft()
    cards.append(cards.popleft())
