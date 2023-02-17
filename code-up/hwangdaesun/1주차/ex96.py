listlist = []

for i in range(3):
    list_s = input().split()
    list_i = list(map(int,list_s))
    listlist.append(list_i)

print(listlist)

a,b = input().split()
a = int(a) - 1
b = int(b) - 1

for i in range(0,len(listlist)):
    for j in range(0,len(listlist[i])):
        if(i == a):
            listlist[i][j] = not listlist[i][j]
        if(j == b):
            listlist[i][j] = not listlist[i][j]
            
print(listlist)
for i in range(0,len(listlist)):
    for j in range(0,len(listlist[i])):
        print(int(listlist[i][j]))
