

import sys
sys.setrecursionlimit(1000000000)
# 두 숫자 선택해서 가장 0과 가까운 값 찾기.
N = int(input())
liquid = list(map(int, sys.stdin.readline().split()))
liquid.sort()
dap = [0, 1, 2, 3]
count = 1000000000


def binary(arr, i, j, count):

    if i >= j:
        return count
    while i < j:
        if arr[i]+arr[j] < 0:
            if abs(count) > abs(arr[i]+arr[j]):
                count = arr[i]+arr[j]
                dap[0] = arr[i]
                dap[1] = arr[j]
             # 0보다 작다 라는건, |arri|>|arrj| 라는 것이고, 이는 이 i 인덱스일때 가장 0에 가까운 값을 뜻함.
             # 예를들어 -99 +98 <0 이고, j +1 하면 -99+4 돼서 -95가 됨. arrj 가 - 라도 마찬가지.(가장 오른쪽에 있는걸 더해야 0과 가까운 수가 됨.)
             # 즉 i 고정하고, j 값 바꿔봤자 더 0과 가까운 값 못얻음.
            i += 1
            binary(arr, i, j, count)
        elif arr[i]+arr[j] > 0:
            if abs(count) > abs(arr[i]+arr[j]):
                count = arr[i]+arr[j]
                dap[0] = arr[i]
                dap[1] = arr[j]
            j -= 1
            binary(arr, i, j, count)

        else:
            print(arr[i], arr[j])


if liquid[0] > 0:  # 전부 양수인 경우
    print(liquid[0], liquid[1])
elif liquid[N-1] < 0:  # 전부 음수인 경우
    print(liquid[N-1], liquid[N-2])
else:
    binary(liquid, 0, N-1, count)
    print(dap[0], dap[1])
