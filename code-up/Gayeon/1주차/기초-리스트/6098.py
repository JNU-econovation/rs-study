
arr=[]
for i in range(10):
    arr.append([])
    arr[i]=list(map(int, input().split()))
x=1
y=1
while x<=8 :
    if arr[x][y]==0:
        arr[x][y]=9
        y+=1
    elif arr[x][y]==1:
        x+=1
        y-=1
    elif arr[x][y]==2:
        arr[x][y] = 9
        break
    elif x==8 and y==8:
        break

for i in range(10):
    for j in range(10):
        print(arr[i][j],end=" ")
    print()

