from collections import deque

# 시작위치 (0,0), 출구 : (n-1,m-1)

n,m = map(int,input().split())
graph = [list(map(int,input()))for _ in range(n)]
print(graph)

queue = deque()
dir = [(1,0),(0,1),(-1,0),(0,-1)]
r = 0
c = 0
count = 0

# 1이면 queue에 담아
if(graph[r][c] == 1):
    queue.append(1)
while(1):
    count += queue.popleft()
    print(count)
    for i in range(len(dir)):
        nr = r + dir[i][0]
        nc = c + dir[i][1]
        if(-1<nr<n and -1<nc<m):
            if (graph[nr][nc] == 1):
                queue.append(1)
                r = nr
                c = nc
                break
        else:
            continue
    print(r,c)
    if(r == n-1 and c == m-1):
        break
print(count+1)