a = list(map(int, input().split()))

for i in range(len(a)):
    if a[i] % 2 == 0:
        print("even")
    else:
        print("odd")


