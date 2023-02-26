t = int(input())

m, n, k = 0, 0, 0

ground = [[0 for j in range(50)] for i in range(50)]
vis = [[0 for j in range(50)] for i in range(50)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x):
    global ground, vis, m, n
    vis[x[0]][x[1]] = 1
    que = []
    que.append(x)
    
    while(len(que) >= 1):
        cur = que[0]
        que.pop(0)
        for i in range(0,4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if vis[nx][ny] == 1 or ground[nx][ny] == 0:
                continue
            vis[nx][ny] = 1
            que.append((nx,ny))
    return


for yy in range(0,t):
    m,n,k = map(int, input().split())

    for i in range(0,50):
        for j in range(0,50):
            ground[i][j] = 0
            vis[i][j] = 0
            
    for i in range(0,k):
        x,y = map(int, input().split())
        ground[x][y] = 1

        
    ans = 0

    for i in range(0,m):
        for j in range(0,n):
            if vis[i][j] == 0 and ground[i][j] == 1:
                bfs((i,j))
                ans += 1
                
    print(ans)
    