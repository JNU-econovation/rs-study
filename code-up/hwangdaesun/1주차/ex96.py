listlist = []

for i in range(19):
    list_s = input().split()
    list_i = list(map(int,list_s))
    listlist.append(list_i)

n = int(input())
for i in range(0,n):
    a,b = input().split()
    a = int(a) - 1
    b = int(b) - 1
    for i in range(0,len(listlist)):
        for j in range(0,len(listlist[i])):
            if(i == a):
                listlist[i][j] = not listlist[i][j]
            if(j == b):
                listlist[i][j] = not listlist[i][j]    

for i in range(0,len(listlist)):
    for j in range(0,len(listlist[i])):
        print(int(listlist[i][j]), end=" ")
    print()

# not을 사용하여 1 <-> 0 변환