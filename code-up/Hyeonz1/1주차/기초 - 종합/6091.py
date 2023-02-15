a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

result = 0
for i in range(max(a, b), (a * b) + 1):
    if i % a == 0 and i % b == 0:
        result = i
        break

for i in range(max(result,c), result * c + 1):
    if i % result == 0 and i % c == 0:
        result = i
        break

print(result)