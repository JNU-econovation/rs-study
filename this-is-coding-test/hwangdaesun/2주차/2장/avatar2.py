n,m = input().split()
n = int(n)
m = int(m)

r,c,d = input().split()

r = int(r)
c = int(c)
d = int(d)

count = 0

map_list = [list(map(int,input().split()))for i in range(m)]
dir = ((-1,0),(0,1),(1,0),(0,-1))
stop = True

while(stop):
    nr = 0
    nc = 0
    for i in range(len(dir)):
        nr = r + dir[(d + i)%4][0]
        nc = c + dir[(d + i)%4][1]
        if(0<nr<m and 0<nc<n):
            if(map_list[nr][nc] == 0):
                if(map_list[nr][nc] != 2):
                    map_list[nr][nc] = 2
                    count += 1
                r = nr
                c = nc
                break
            else:
                continue
    r = r + -1*dir[(d+i)%4][0]
    c = c + -1*dir[(d+i)%4][1]
    if(map_list[r][c] == 1):
        stop = False
        break
print(count)