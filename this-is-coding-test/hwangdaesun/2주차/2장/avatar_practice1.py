n = int(input())

m = 1
k = 1

clist = input().split()

for i in range(len(clist)):

    if(clist[i] == 'L'):
        if(k == 1):
            continue
        k -=1
    elif(clist[i] == 'R'):
        if(k == 5):
            continue
        k +=1
    elif(clist[i] == 'U'):
        if(m == 1):
            continue
        m -=1
    elif(clist[i] == 'D'):
        if(m == 5):
            continue
        m +=1
print(m,k,end=" ")