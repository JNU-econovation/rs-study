ki = [int(input())for _ in range(9)]

ki.sort(reverse= True)
stop = False
for i in range(8):
    for j in range(i+1,9):
        a = ki.pop(j)
        b = ki.pop(i)
        if(sum(ki) == 100):
            stop = True
            break
        else:
            ki.append(a)
            ki.append(b)
            ki.sort(reverse=True)
    if(stop):
        break

ki.sort()
for i in range(7):
    print(ki[i])




