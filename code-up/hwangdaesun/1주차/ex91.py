a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

i = 1
while i%a!=0 or i%b!=0 or i%c!=0:
  i += 1

print(i)