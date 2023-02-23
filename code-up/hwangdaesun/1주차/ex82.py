a = int(input())
for i in range(1,a+1):
    if(i%10 == 3):
        print("X", end=" ")
        continue
    elif(i%10 == 6):
        print("X", end=" ")
        continue
    elif(i%10 == 9):
        print("X", end=" ")
        continue
    else:
        print(i, end=" ")

#문제 이해 미숙