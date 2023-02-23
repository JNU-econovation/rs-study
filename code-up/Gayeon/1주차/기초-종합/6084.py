a, b, c, d = input().split(" ")
a = int(a)
b= int(b)
c= int(c)
d= int(d)
k=a*b*c*d/8/1024/1024
print(f"{k:0.1f} MB")