n,m = input().split()
n = int(n)
m = int(m)

ilist = [list(map(int, input().split())) for _ in range(n)]

minlist = []


for n in range(n):
    minlist.append(min(ilist[n]))

print(minlist)
minlist.sort(reverse=True)
print(minlist[0])
            