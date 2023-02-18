a, m, d, n = map(int, input().split())

for i in range(n):
    a *= m
    a += d

print(a)