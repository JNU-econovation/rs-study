a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

for x in range(0, a):
    for y in range (0, b):
        for z in range(0, c):
            print(x, y, z)

print(a*b*c)