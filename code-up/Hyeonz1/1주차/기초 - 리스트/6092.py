total = int(input())
order = input().split()
count = []

for i in range(total):
    order[i] = int(order[i])

for i in range(0, 23):
    count.append(0)

for i in range(total):
    count[order[i]-1] += 1

for i in range(0, 23):
    print(count[i], end = ' ')
