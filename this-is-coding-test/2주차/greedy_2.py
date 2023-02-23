# 숫자 카드 게임

# 가장 높은 숫자의 카드 뽑기. 선택한 행중 가장 낮은 카드 뽑아야 한다.
# 즉 각 행 중 가장 작은 숫자들을 뽑고, 그 숫자카드 중 가장 큰 카드를 뽑는다.

N, M = input().split()
card_list = [list(map(int, input().split())) for _ in range(int(N))]
# -> 2차원 배열 입력받기. _in range는 그냥 n번 입력받는다는 뜻.
smallest = []
for i in range(int(N)):
    card_list[i].sort(reverse=False)
    smallest.append(card_list[i][0])

smallest.sort(reverse=True)
print(smallest[0])






