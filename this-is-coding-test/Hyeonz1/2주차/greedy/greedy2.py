n, m = map(int, input().split())

cards = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    cards[i].sort()
cards.sort()

print(cards)
mymax = 0

for i in range(n - 1):
    mymax = max(cards[i][0], cards[i + 1][0])

print(mymax)