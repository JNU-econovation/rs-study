h,w = input().split()
h = int(h)
w = int(w)
listlist = [[0 for j in range(h)] for i in range(w)]

n = int(input())

for i in range(n):
    l,d,x,y = input().split()
    l = int(l)
    d = int(d)
    x = int(x) - 1
    y = int(y) - 1
    for i in range(l):
        if(d == 0):
            listlist[x][y+i] = 1
        else:
            listlist[x+i][y] = 1
            
for i in range(len(listlist)):
    for j in range(len(listlist[i])):
        print(int(listlist[i][j]), end=" ")
    print()