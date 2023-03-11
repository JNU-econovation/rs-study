list = input().split()
for i in range(len(list)):
    if(int(list[i]) % 2 == 0):
        print(list[i])

# 그냥 input()의 경우에는 빈 문자열까지 list에 포함된다.
