a, b, c= input().split(" ")
a= int(a)
b= int(b)
c= int(c)
k=a*b*c/8/1024/1024
print(f"{k:0.2f} MB")