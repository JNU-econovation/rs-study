# 양수만 있을때, 음수만 있을때는 따로(양수는 가장 첫번째 두개가 0과 가까움, 음수는 가장 끝 두개가 0과 가까움.)
# 음,양수 따로 뺴서 이진탐색하기

#  mid , mid+1 값과 더해서 비교 후 <0 과 >0 이 나오면 그 두 값 중 작은 값의 mid와 -99를 순서대로 배열에 넣기.
#                                           더한 값도 선언해서 넣어주기.
# <0 <0 나오면 오른쪽에서 탐색 다시 해주기.  >0 >0 이면 왼쪽에서 탐색 다시 해주기
#    이 탐색을 - 값들 모두 해주면서 만약 선언된 더한 값보다 탐색 후 찾은 값이 더 작으면 수정해주기.
#    선언해줄거는 출력할 값 배열 1 과 더한값 2

import sys
sys.setrecursionlimit(1000000)

N = int(input())
liquid = list(map(int, sys.stdin.readline().split()))
liquid.sort()
minus_array = []
plus_array = []

count = 1000000000
dap = [1, 2]


def binary(arr, target, start, end, count):
    if start >= end:
        if count > abs(arr[end]+target):
            count = abs(arr[end]+target)
            dap[0] = arr[end]
            dap[1] = target
            return count

    while start < end:
        mid = (start+end)//2
        if arr[mid]+target == 0:
            count = 0
            dap[0] = target
            dap[1] = arr[mid]
            return count
        elif arr[mid+1]+target == 0:
            count = 0
            dap[0] = target
            dap[1] = arr[mid+1]
            return count
        elif arr[mid]+target < 0 and arr[mid+1]+target < 0:
            binary(arr, target, mid+1, end, count)
        elif arr[mid]+target > 0 and arr[mid+1]+target > 0:
            binary(arr, target, start, mid, count)
        else:
            if arr[mid]+target >= arr[mid+1]+target:
                if count > abs(arr[mid+1]+target):
                    count = abs(arr[mid+1]+target)
                    dap[0] = target
                    dap[1] = arr[mid+1]
                    return count
                else:
                    break
            else:
                if count > abs(arr[mid]+target):
                    count = abs(arr[mid]+target)
                    dap[0] = target
                    dap[1] = arr[mid]
                    return count
                else:
                    break


if liquid[0] > 0:  # 전부 양수인 경우
    print(liquid[0], liquid[1])
elif liquid[N-1] < 0:  # 전부 음수인 경우
    print(liquid[N-1], liquid[N-2])
else:
    for i in range(N):  # -, + 나누기.
        if liquid[i] < 0:
            minus_array.append(liquid[i])
        else:
            plus_array.append(liquid[i])
    # + 어레이 앞 두개 인덱스 더한거 랑 -어레이 맨 뒤 두개 더한거
    minus_array.sort()
    plus_array.sort()
    if len(minus_array) >= 2:
        count = abs(minus_array[len(minus_array)-1] +
                    minus_array[len(minus_array)-2])
        dap[0] = minus_array[len(minus_array)-1]
        dap[1] = minus_array[len(minus_array)-2]
    if len(plus_array) >= 2:
        if count > abs(plus_array[0]+plus_array[1]):
            count = abs(plus_array[0]+plus_array[1])
            dap[0] = plus_array[0]
            dap[1] = plus_array[1]
# 플러스 어레이랑 마이너스 어레이 각각 더해서 최소가 된 값 미리 넣어두기.
    for i in range(len(minus_array)):
        count = abs(
            binary(plus_array, minus_array[i], 0, len(plus_array)-1, count))

dap.sort()
print(dap[0], dap[1])
