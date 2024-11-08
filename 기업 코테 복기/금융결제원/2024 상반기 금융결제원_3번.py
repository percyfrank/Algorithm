from collections import defaultdict


def backtracking(idx, cnt, total):
    global answer

    if cnt == row:
        answer = min(answer, total)
        return

    # 내가 가지고 있는 카드랑 같은 갯수 만큼 점수 증가
    tmp = 0
    for card in cards[idx]:
        if card in my_card.keys():
            tmp += my_card[card]

    for i in range(col):
        if not visited[idx][i]:
            visited[idx][i] = True
            my_card[cards[idx][i]] += 1
            backtracking(idx + 1, cnt + 1, total + tmp)
            visited[idx][i] = False
            my_card[cards[idx][i]] -= 1

n = int(input())
cards = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')
row, col = len(cards), len(cards[0])
visited = [[False for _ in range(col)] for _ in range(row)]
my_card = defaultdict(int)
backtracking(0, 0, 0)
print(answer)

#### 문제
# n = 게임 턴 횟수
# cards = 게임 턴 마다 뽑은 카드 조합
# 매 턴마다 카드 조합을 새로 뽑는다. 규칙은 다음과 같다.
# 카드 조합 내의 각각의 숫자를 내가 가지고 있는 카드와 비교했을 때 같다면 같은 갯수만큼 점수 증가.
# 그런 다음, 카드 조합 중 1장은 내 카드로 가져감.
# 모든 턴을 지났을 때 얻은 점수의 최솟값 구하기

#### 조건
# cards의 길이 <= 10000
# cards[i]의 길이 <= 100

#### 입력
# 5
# 1 2 5 1 2 => 5            => +0
# 3 1 3 3 2 => 1            => +0
# 3 3 3 5 2 => 5            => +1
# 2 2 2 4 3 => 3            => +0
# 1 2 4 1 1 => 상관없음       => +3

#### 출력 : 4점

#### 입력
# 4
# 2 10 => 10
# 2 2  => 2
# 2 2  => 2
# 2 2  => 상관없음

#### 출력 : 6점

#### 입력
# 3
# 3 1 2 3 => 1
# 3 3 2 3 => 2
# 3 3 3 3 => 상관없음

#### 출력 : 0점
