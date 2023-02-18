# 내용 : 나올 수 있는 주사위의 숫자를 오름차순으로 출력한다.
n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        print(i + 1, j + 1)
