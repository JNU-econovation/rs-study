total = int(input())
order = input().split()

for i in range(len(order)):
    order[i] = int(order[i])

print(min(order))