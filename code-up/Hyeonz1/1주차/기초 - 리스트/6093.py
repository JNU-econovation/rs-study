total = int(input())
order = input().split()

for i in range(total):
    order[i] = int(order[i])

for i in range(total):
    print(order[total-1-i], end = ' ')