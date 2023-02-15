n = input()
n = int(n, 16)
for i in range(1, 16):
    print('%X'%n, "*", '%X'%i, "=", '%X'%(n*i), sep='')

# print문에서 seperator를 지정
# seperator를 지정하지 않으면 각 변수 사이에 띄어쓰기가 입력된다.