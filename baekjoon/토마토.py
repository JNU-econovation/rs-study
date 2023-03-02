import sys
from collections import deque

m,n,h = map(int,input().split())

box = [[list(map(int,sys.stdin.readline().split()))for _ in range(n)]for _ in range(h)]
dir = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

queue = deque()

def bfs(i,j,k):
    for d in range(len(dir)):
        ii = i + dir[d][0]
        jj = j + dir[d][1]
        kk = k + dir[d][2]
        if(-1<ii<h and -1<jj<n and -1<kk<m):
            if(box[ii][jj][kk] == 0):
                queue.append((ii,jj,kk))  
                


b = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if(box[i][j][k] == 0):
                b +=1
if(b==0):
    print(0)
    sys.exit()

count = 0
stop = False

while(1):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if(box[i][j][k] == 1):
                    bfs(i,j,k)
                    if queue:
                        a = queue.popleft()
                        box[a[0]][a[1]][a[2]] = 1
                        count += 1
                    else:
                        stop = True
    if(stop):
        break


print(box)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if(box[i][j][k] == 0):
                print(-1)
                sys.exit()
                
        
print(count)

# bfs에서의 함수는 방문을 했는 지의 여부를 확인한다




    