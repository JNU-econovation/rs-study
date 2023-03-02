from collections import deque

N = int(input())

color_list = []

for i in range(N):
    color_list.append(list(input()))        

handi_list = [['']*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if color_list[i][j] == 'G':
            handi_list[i][j] = 'R'
        else:
            handi_list[i][j] = color_list[i][j]

#상 하 좌 우
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

def bfs(arr, x, y, alpha):
    
    q = deque()
    q.append((x, y))
    
    arr[x][y] = 'visited'
    
    while q:
        
        x, y = q.popleft()
        
        for i in range(4):
            new_x = x + dx[i] 
            new_y = y + dy[i]
            
            if new_x >= N or new_x < 0 or new_y >= N or new_y < 0:
                continue
            
            if arr[new_x][new_y] == alpha:
                arr[new_x][new_y] = 'visited'
                q.append((new_x, new_y))
                    
    return

normal_cnt = 0
handi_cnt = 0

for i in range(N):
    for j in range(N):
        if color_list[i][j] == 'R':
            bfs(color_list, i, j, 'R')
            normal_cnt += 1            
                    
        elif color_list[i][j] == 'G':
            bfs(color_list, i, j, 'G')
            normal_cnt += 1    
            
        elif color_list[i][j] == 'B':
            bfs(color_list, i, j, 'B')
            normal_cnt += 1  
                    
for i in range(N):
    for j in range(N):
        if handi_list[i][j] == 'R':
            bfs(handi_list ,i, j, 'R')
            handi_cnt += 1            
            
        elif handi_list[i][j] == 'B':
            bfs(handi_list, i, j, 'B')
            handi_cnt += 1  
            
print(normal_cnt, handi_cnt)
            