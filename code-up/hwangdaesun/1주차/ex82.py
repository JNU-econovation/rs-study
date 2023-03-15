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

# 문제 이해 미숙
# 코드 개선 -> 조건문을 한 줄에 나타낼 수 있음 if i % 10 == 3 or i % 10 == 6 or i % 10 == 9