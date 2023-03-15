a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
sum = a + b + c
average = sum/3

print(sum,"%.2f"%average,end=" ")

# 기본적으로 print()함수에서는 디폴트로 end = "\n"가 설정되어 있음
