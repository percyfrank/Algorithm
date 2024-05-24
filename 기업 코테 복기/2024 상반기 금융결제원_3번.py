from collections import defaultdict


def dfs(idx, cnt, total, arr):
    global answer

    if cnt == row:
        answer = min(answer, total)
        return

    # 내가 가지고 있는 카드랑 가은 갯수 만큼 점수 증가
    tmp = 0
    for card in cards[idx]:
        if card in my_card.keys():
            tmp += my_card[card]

    for i in range(col):
        if not visited[idx][i]:
            visited[idx][i] = True
            my_card[cards[idx][i]] += 1
            arr.append((idx, i))

            dfs(idx + 1, cnt + 1, total + tmp, arr)

            visited[idx][i] = False
            my_card[cards[idx][i]] -= 1
            arr.pop()


n = int(input())
cards = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')
row, col = len(cards), len(cards[0])
visited = [[False for _ in range(col)] for _ in range(row)]
my_card = defaultdict(int)
dfs(0, 0, 0, [])
print(answer)

#### 문제
# n = 게임 턴 횟수
# cards = 게임 턴 마다 뽑은 카드 조합
# 매 턴마다 카드 조합을 새로 뽑고, 내가 가지고 카드랑 같은 갯수만큼 점수 증가
# 매 턴마다 카드 조합을 뽑게되면 그 중 1장은 내 카드로 가져가야 함
# 모든 턴을 지났을 때 얻은 점수의 최솟값 구하기

#### 입력 조건
# cards의 길이 <= 10000
# cards[i]의 길이 <= 100

# 5
# 1 2 5 1 2 => 5
# 3 1 3 3 2 => 1
# 3 3 3 5 2 => 5
# 2 2 2 4 3 => 3
# 1 2 4 1 1 => 상관없음

# 출력 : 4점

# 4
# 2 10 => 10
# 2 2  => 2
# 2 2  => 2
# 2 2  => 상관없음

# 출력 : 6점

# 3
# 3 1 2 3 => 1
# 3 3 2 3 => 2
# 3 3 3 3 => 상관없음

# 출력 : 0점
