a, b, c = input().split(" ")
a= int(a)
b= int(b)
c= int(c)
num=0
for i in range(0,a):
    for j in range(0,b):
        for y in range(0,c):
            print(i,j,y)
            num +=1
print(num)