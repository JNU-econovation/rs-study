import sys

n,m = map(int, input().split())

dduck = list(map(int,sys.stdin.readline().strip().split()))

dduck.sort()

start = 0
end = max(dduck) - 1

after_cut = []

def cut(array,height):
    after_cut.clear()
    for i in range(len(array)):
        if(array[i] > height):
            after_cut.append(array[i] - height)
        else:
            after_cut.append(0)
    return after_cut


while(start <= end):
    mid = (start + end) // 2
    hap = sum(cut(dduck,mid))
    if(start == end):
        print(start)
        break
    if(hap > m):
        start = mid + 1
    elif(hap < m):
        end = mid - 1
    else:
        print(start)