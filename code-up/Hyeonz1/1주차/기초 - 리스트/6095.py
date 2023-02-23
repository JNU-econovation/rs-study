count = int(input())
coordinate = []

for i in range(19):
    coordinate.append([])
    for j in range(20):
        coordinate[i].append(0)

for i in range(count):
    x, y = input().split()
    coordinate[int(x)-1][int(y)-1] = 1

for i in range(19):
    for j in range(19):
        print(coordinate[i][j], end = ' ')
    print()
