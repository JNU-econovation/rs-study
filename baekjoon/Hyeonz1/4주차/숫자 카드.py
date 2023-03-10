# 숫자 카드

# 입력
total_card = int(input())
cards = list(map(int, input().split()))
total_compare_deck = int(input())
compare_deck = list(map(int, input().split()))

# 정렬
cards.sort()

# 이진 탐색 함수 구현
def binary_search(array, target, start, end):
    if start > end:
         return 0
    mid = (start + end) // 2
    if array[mid] == target:
         return 1
    elif array[mid] > target:
         return binary_search(array, target, start, mid - 1)
    else:
         return binary_search(array, target, mid + 1, end)


for comparisons in range(total_compare_deck):
    print(binary_search(cards, compare_deck[comparisons], 0, total_card - 1), end = ' ')
     