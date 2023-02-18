# 내용 : 1부터 num까지 출력하되, 3의 배수가 있는 경우는 X가 출력
    # 일의 자리에 3의 배수가 있는 경우에는 X가, 아닐 때는 숫자가 그대로 출력되어야 한다.

num = int(input())

for i in range(num):
    if (i%10 == 0 and i%3 == 0):
        print("X", end = ' ')
    elif (i%10 != 0 and i%10%3 == 0):
        print("X", end = ' ')
    else:
        print(i, end =' ')
        