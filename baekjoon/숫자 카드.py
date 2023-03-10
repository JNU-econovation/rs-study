# 상근 n개
# 정수 m개 주어짐
# 상근이가 가지고 있는 지 아닌지를 구하라

import sys

n = int(input())
have = list(map(int,sys.stdin.readline().strip().split()))
m = int(input())
want = list(map(int,sys.stdin.readline().strip().split()))

have.sort()

def search(array,target,start,end):
    if(start>end):
        return 0
    mid = (start + end)//2
    if(array[mid] == target):
        return 1
    elif(array[mid] > target):
        return search(array,target,start,mid-1)
    else:
        return search(array,target,mid+1,end)

for i in range(m):
    if search(have,want[i],0,len(have)-1) == 1:
        print(1, end =" ")
    else:
        print(0, end= " ")

# 정렬 필수!