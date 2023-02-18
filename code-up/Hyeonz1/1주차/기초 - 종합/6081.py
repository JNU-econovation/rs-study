# 내용 : 16진수 구구단 출력
    # 1. 16진수 입력받기
    # 2. 16진수 구구단 출력하기
n = int(input(), 16)
for i in range(1, 16):
    print('%X'%n, "*", '%X'%i, "=", '%X'%(n*i), sep='')

# 인상깊었던 점
# print문에서 seperator를 지정
# seperator를 지정하지 않으면 각 변수 사이에 띄어쓰기가 입력된다.