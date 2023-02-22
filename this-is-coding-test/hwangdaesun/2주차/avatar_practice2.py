n = input()
count = 0

for h in range(int(n)+1):
    for m in range(60):
        for s in range(60):
            if n in str(h) + str(m) + str(s):
                count += 1
print(count)