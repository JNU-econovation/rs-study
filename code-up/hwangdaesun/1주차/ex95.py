n = int(input())

list = [[0 for j in range(20)] for i in range(20)]

for i in range(0,n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    list[a][b]=1

for i in range(1,20):
    for j in range(1,20):
        print(list[i][j], end =" ")
    print()


# list = [[0 for j in range(20)] for i in range(20)]는  for i in range(20)에서 i가 20개가 만들어지고, [0 for j in range(20)]를 20번 반복하는 것이다.
# 그리고, 0 for j in range(20)는 20개의 0으로 list를 초기화해준다는 뜻 