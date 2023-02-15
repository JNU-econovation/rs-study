number = int(input())
n = 1
sum = n * (n + 1) / 2

while number > sum:
    n += 1
    sum = n * (n + 1) / 2

print(int(sum))