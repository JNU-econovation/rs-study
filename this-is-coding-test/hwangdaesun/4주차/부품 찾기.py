import sys

n = int(input())
have = list(map(int,input().split()))
m = int(input())
want = list(map(int,input().split()))

have.sort()

def search(array,target,start,end):
    if(start > end):
        return None
    mid = (start + end) // 2
    if(array[mid] == target):
        return True
    elif(array[mid] > target):
        return search(array,target,start,mid-1)
    else:
        return search(array,target,mid+1,end)
    

for i in range(m):
    if(search(have,want[i],0,4) == True):
        print("yes", end=" ")
    else:
        print("no", end=" ")