# 6006
print("\"!@#$%^&*()\'")

# 6007
print('\"C:\\Download\\\'hello\'.py\"')

#6008
print('print(\"Hello\\nWorld\")')

#6013
a=input()
b=input()
print(b)
print(a)

#6019
y,m,d = input().split('.')
print(d+'-'+m+"-"+y)

# 6026
a = float(input())
b= float(input())
print(a+b)

# 6031
a = int(input())
print(chr(a))

#6033
a = ord(input())
print(chr(a+1))

#6038
a, b = input().split(' ')
print(int(a)**int(b))

# 6046
a = int(input())
print(a<<1)

# 6047
a, b = input().split(' ')
print(int(a)<<int(b))
# 6048
a, b = input().split(' ')
if int(a)<int(b) :
    print('True')
else :
    print('False')
#6051
a, b = input().split(' ')
if int(a)!=int(b) :
    print('True')
else :
    print('False')
#6054
a, b = input().split(' ')
if bool(int(a)) and bool(int(b)):
    print('True')
else:
    print('False')
#6056
a, b = input().split(' ')
if bool((int(a) and (not int(b))) or ((not int(a)) and int(b))):
    print('True')
else:
    print('False')
#6059
a = input()
print(~int(a))
#6060
a, b = input().split(' ')
print(int(a) & int(b))
#6063
a, b = input().split(' ')
a = int(a)
b = int(b)
print(int(a if (a >= b) else b))
#6064
a, b, c = input().split(' ')
a=int(a)
b=int(b)
c=int(c)
print((a if a<b else b) if ((a if a<b else b)<c) else c)

#6066
a, b, c = input().split(' ')
a=int(a)
b=int(b)
c=int(c)
def evenOdd(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
evenOdd(a)
evenOdd(b)
evenOdd(c)
#6069
a = input()
if a=='A':
    print('best!!!')
elif a=='B':
    print('good!!')
elif a=='C':
    print('run!')
elif a=='D':
    print('slowly~')
else:
    print('what?')
#6073
a = int(input())
while a > 0:
    a = a - 1
    print(a)
#6075
a = int(input())
n = 0
while a >= n:
    print(n)
    n = n+1
#6077
a = int(input())
n = 0
for i in range(1, a+1):
  if i%2==0 :
    n += i

print(n)

#6078
i = input()
while i != 'q':
  print(i)
  i = input()
print(i)
#6079
n = int(input())
hap = 0
i = 1
while hap < n:
  hap += i
  i += 1

print(i-1)

#6080
n, m = input().split(' ')
n = int(n)
m = int(m)
for i in range(1,n+1):
  for j in range(1,m+1):
    print(i,j)

# 종합 6082
k = input()
y = int(k, 16)  # k를 16진수로
for i in range(1,16):
    print(f'{y:X}*{i:X}={i*y:X}')

# 종합 6082
k = int(input())
for i in range(1,k+1):
    if i%10==3:
        print("X",end=" ")  # end는 줄바꿈없이출력가능
    elif i%10==6:
        print("X",end=" ")
    elif i%10==9:
        print("X",end=" ")
    else:
        print(i,end=" ")

# 종합 6083