from collections import deque
import sys
n,m = map(int,input().split())

miro = [[list((map(int,sys.stdin.readline().strip()))),[1]*m]for _ in range(n)]
queue = deque()
dir = ((1,0),(0,1),(0,-1),(-1,0))

def bfs():
    count = 1
    queue.append((0,0))
    while(queue):
        r,c = queue.popleft()
        if(r == n-1 and c == m-1):
            return count,True
        for k in range(4):
            nr = r + dir[k][0]
            nc = c + dir[k][1]
            if(-1<nr<n and -1<nc<m and miro[nr][0][nc] == 0 and miro[nr][1][nc] == 1):
                queue.append((nr,nc))
                count += 1
                miro[nr][1][nc] = 0
                break
    return count,False

shortL = []

for i in range(n):
    for j in range(m):
        if(miro[i][0][j] == 1):
            miro[i][0][j] = 0
            count,isShort = bfs()
            miro[i][0][j] = 1
            if(isShort):
                shortL.append(count)
        miro[i][1][j] = 1

if(len(shortL) == 0):
    print(-1)
else:
     print(min(shortL))

