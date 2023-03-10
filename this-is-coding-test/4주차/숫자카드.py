import sys
N = int(input())
my_cards = list(map(int, sys.stdin.readline().split()))
M = int(input())
your_cards = list(map(int, sys.stdin.readline().split()))
# list(map(int, sys.stdin.readline().rstrip())) 로 해주면 input보다 빠르다고 함.
# array 는 오름차순으로 정렬해주기~
my_cards.sort()


def binary(array, target, start, end):
    if start > end:  # 첫번째 인덱스가 마지막 인덱스보다 커지면 종료
        return None
    while start <= end:
        mid = (start + end)//2  # 중간 인덱스 설정(소수점 나오면 안되니깐 몫만 나오게하기)
        if array[mid] == target:  # 배열의 가운데가 찾고자 하는 것과 같으면 종료.(찾은거니깐)
            return mid
        elif array[mid] > target:  # 배열의 가운데가 찾고자하는것보다 크면 찾고자 하는게 가운데보다 왼쪽에 있다는것
            # 이므로 end=mid-1 로 설정 후 재귀
            return binary(array, target, start, mid - 1)
        else:
            return binary(array, target, mid + 1, end)


for i in range(M):
    result = binary(my_cards, your_cards[i], 0, N-1)
    if result == None:
        print("0", end=" ")
    else:
        print("1", end=" ")
