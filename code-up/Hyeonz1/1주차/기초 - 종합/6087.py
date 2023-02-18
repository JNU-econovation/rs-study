# 내용 : 1부터 입력받은 수까지 출력하되, 3의 배수는 출력되면 안됨.
num = int(input())

for i in range(1, num + 1):
    if i % 3 == 0 :
        continue
    print(i, end=' ')

# if-else문 대신 continue 사용