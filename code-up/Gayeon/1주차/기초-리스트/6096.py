arr=[]
for i in range(19):
    arr.append([])
    arr[i]=list(map(int, input().split()))


n = int(input())
for i in range(n):
    x,y= input().split()
    for j in range(0,19):
        if arr[j][int(y)-1] == 0: # x값 고정 y값 바뀜-> 가로줄
            arr[j][int(y)-1] = 1
        else:
            arr[j][int(y)-1] = 0

        if arr[int(x)-1][j] == 0: # y값 고정 x값 바뀜-> 세로줄
            arr[int(x)-1][j] = 1
        else:
            arr[int(x)-1][j] = 0

for i in range(19):
    for j in range(19):
        print(arr[i][j],end=" ")
    print()

