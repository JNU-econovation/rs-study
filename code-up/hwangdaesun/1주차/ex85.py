w,h,b = input().split()
w = int(w)
h = int(h)
b = int(b)

result = w*h*b/8/1024/1024
print(f"{result:.2f} MB")