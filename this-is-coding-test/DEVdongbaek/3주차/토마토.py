from collections import deque

M, N, H = map(int, input().split())

graph = []

q = deque([])

day = 0

# 2 차원 입력을 H를 기준으로 2차원으로 나눠서 3차원 리스트 작성
for i in range(H):
    
    tmp = []
    
    # N -> 3, M -> 5
    for j in range(N):
        tmp.append(list(map(int, input().split())))
        
        for k in range(M):
            
            # tmp에 추가된 리스트의 원소 중 1이면 큐에 추가
            if tmp[j][k] == 1:
                q.append([i, j, k])
    
    # 2차원 배열인 tmp를 graph에 추가하면서 3차원 배열 만들기
    graph.append(tmp)

# 3차원 방향 설정
dx = [-1, +1, 0, 0, 0, 0]
dy = [0, 0, -1, +1, 0, 0]  
dz = [0, 0, 0, 0, -1, +1]


while q:
    x, y, z = q.popleft()
    
    for i in range(6):
    
        new_x = x + dx[i]
        new_y = y + dy[i]
        new_z = z + dz[i]
    
        if 0 <= new_x < H and 0 <= new_y < N and 0 <= new_z < M and graph[new_x][new_y][new_z] == 0:
            # 비교한 토마토에 기존 토마토 + 1 --> 하루 지나는 것 구현
            graph[new_x][new_y][new_z] = graph[x][y][z] + 1
            q.append([new_x, new_y, new_z])



for i in graph:
    for j in i:
        for k in j:
            # 큐로 while문을 돌렸음에도 0이 있다면 토마토가 익지 못 하는 상황
            if k == 0:
                print(-1)
                exit()
        day = max(day, max(j))

# 처음부터 익은 토마토가 존재하고, 따라서 시작점이 1이기 때문에 day -1
print(day-1)