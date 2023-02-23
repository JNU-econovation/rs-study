n = int(input())
list_s = input().split()
list = list(map(int, list_s))

for i in range(1,24):
    print(list.count(i), end=" ")