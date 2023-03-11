n = input()
r = ord(n[:1])-ord('a')+1
c = int(n[1:])
count = 0
dir = ((1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1))

for d in range(len(dir)):
    nr =0
    nc = 0
    nr = r + dir[d][0]
    nc = c + dir[d][1]
    if(0<nr<9 and 0<nc<9):
        count +=1
print(count)

# 주의해야할 점 : nr과 nc의 제한 범위가 1과 8이아닌 0과 9이다.

