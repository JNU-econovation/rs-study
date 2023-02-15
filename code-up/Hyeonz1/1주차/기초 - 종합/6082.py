num = int(input())

for i in range(1, num+1):
    if (i%10 == 0 and i%3 == 0):
        print("X", end = ' ')
    elif (i%10 != 0 and i%10%3 == 0):
        print("X", end = ' ')
    else:
        print(i, end =' ')