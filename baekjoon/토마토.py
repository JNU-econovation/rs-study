import sys
from collections import deque

m,n,h = map(int,input().split())

box = [[list(map(int,sys.stdin.readline().split()))for _ in range(n)]for _ in range(h)]
dir = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

queue = deque()

def bfs(i,j,k):
    queue.append((i,j,k))
    while(queue):
        ii,jj,kk = queue.popleft()
        for d in range(len(dir)):
            ai = ii + dir[d][0]
            aj = jj + dir[d][1]
            ak = kk + dir[d][2]
            if(-1<ai<h and -1<aj<n and -1<ak<m):
                if(box[ai][aj][ak] == 0):
                    queue.append((ai,aj,ak))
                    box[ai][aj][ak] = box[ii][jj][kk] + 1 
    
                

for i in range(h):
    for j in range(n):
        for k in range(m):
            if(box[i][j][k] == 1):
                bfs(i,j,k)
count = 0

for i in range(h):
    for j in range(n):
        num = max(box[i][j])
        if(num > count):
            count = num
        for k in range(m):
            if(box[i][j][k] == 0):
                print(-1)
                sys.exit()


print(count-1)





    