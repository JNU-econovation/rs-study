listlist = []

for i in range(10):
    l = input().split()
    l = list(map(int,l))
    listlist.append(l)

x = 1
y = 1

while(1):
    
    if(listlist[x][y] == 0):
        listlist[x][y] = 9
        y = y + 1
    elif(listlist[x][y] == 1):
        y = y - 1
        x = x + 1
        continue
    elif(listlist[x][y] == 2):
        listlist[x][y] = 9
        break
    elif(x == 8 and y == 8):
        break
        
for i in range(len(listlist)):
    for j in range(len(listlist[i])):
        print(listlist[i][j], end = " ")
    print()

