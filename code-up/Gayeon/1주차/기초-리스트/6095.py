arr=[]
for i in range(19):
    arr.append([])
    for j in range(19):
        arr[i].append("0")
n = int(input())
for i in range(n):
    x, y = input().split()
    arr[int(x)-1][int(y)-1]='1'
for i in range(19):
    for j in range(19):
        print(arr[i][j],end=" ")
    print()
