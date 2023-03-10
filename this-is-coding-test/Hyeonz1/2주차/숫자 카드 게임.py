n, m = map(int, input().split())

cards = [list(map(int, input().split())) for _ in range(n)]

# cards[i]의 min값을 비교해서 가장 높은 값이 있는 행i값을 선택한다.
    # cards[i]를 오름차순으로 정렬한다.
    # cards[i][0]를 비교해서 가장 큰 값을 찾는다.

for i in range(n):
    cards[i].sort()

mymax = 0

for i in range(n - 1):
    mymax = max(cards[i][0], cards[i + 1][0])

print(mymax)