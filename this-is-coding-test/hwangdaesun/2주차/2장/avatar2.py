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

# 이 문제를 풀기 위한 파이선 문법 및 아이디어 정리
# 입력 받은 값으로 이중 리스트 만들기
# 행,열 => y,x 인 것 인지
# 이동할 수 있는 방향 -> 튜플을 이용함
# stop이란 변수 -> while문 빠져갈 수 있게함
# 이중 리스트 밖으로 이동 못 하게 제한을 둬야함
# 방문한 곳은 표시를 해둬야함
