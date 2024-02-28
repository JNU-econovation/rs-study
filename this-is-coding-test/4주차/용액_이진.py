
import sys
sys.setrecursionlimit(1000000000)

N = int(input())
liquid = list(map(int, sys.stdin.readline().split()))
liquid.sort()
k = 3000000000
a = 0
b = 0


def binary(arr, target, start, end):   # target = - (-99)=99
    if start >= end:
        return start

    mid = (start+end)//2
    # if arr[mid] == target:
    #     print(-target, arr[mid])
    #     exit()
    if arr[mid] < target:  # 타겟이 mid보다 크다는것 -> 오른쪽에서 재귀.
        # if dap[2] > abs(arr[mid]-target):
        #     dap[2] = arr[mid]-target
        #     dap[0] = target
        #     dap[1] = arr[mid]
        return binary(arr, target, mid+1, end)  # start = 1

    else:
        # if dap[2] > abs(arr[mid]-target):
        #     dap[2] = arr[mid]-target
        #     dap[0] = target
        #     dap[1] = arr[mid]
        return binary(arr, target, start, mid)


for i in range(N):

    bin = binary(liquid, -(liquid[i]), 0, N-1)

    if k > abs(liquid[bin]+liquid[i]) and bin != i:
        a = (liquid[i])
        b = liquid[bin]
        k = abs(a+b)
    if bin == 0:
        continue
    if k > abs(liquid[bin-1]+liquid[i]) and bin-1 != i:
        a = (liquid[i])
        b = liquid[bin-1]
        k = abs(a+b)
if a > b:
    a, b = b, a

print(a, b)
