h,b,c,s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)

result = (h*b*c*s)/8/1024/1024
print("%.1f MB"%result)
print(f'{result:.1f} MB')


# 파이썬 f string의 사용방법, float precision 표현 법