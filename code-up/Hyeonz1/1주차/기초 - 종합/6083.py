a, b, c = map(int, input().split())

for x in range(a):
    for y in range (b):
        for z in range(c):
            print(x, y, z)

print(a*b*c)