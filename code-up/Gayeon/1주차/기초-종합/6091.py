a, b, c= input().split()
a= int(a)
b= int(b)
c= int(c)
day=1
# day 를 a,b,c로 나눴을때 전부 나머지가 0이어야 함.
while not(day%a ==0 and day%b ==0 and day%c ==0):
    day +=1
print(day)

