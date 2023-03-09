from collections import deque
    
# 상, 하, 좌, 우
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]          

def bfs(x, y):
    
    q = deque()
    
    # x, y 좌표와 벽 부수는 기술이 아직 있는지
    q.append([x, y, True])
    
    while q:
        
        x, y, one_punch = q.popleft()
        
        if x == N - 1 and y == M - 1:
            return visited[x][y][one_punch]

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
                continue 
            
            # 벽을 부수지 않았고, 벽을 만났다면 -> 벽을 부수고 이동해준다.
            # 벽을 부수는 스킬을 다 사용했기에 q에 False값을 넣어준다.
            # [True] == [1]
            if one_punch and graph[new_x][new_y]:
                visited[new_x][new_y][False] = visited[x][y][True] + 1
                q.append([new_x, new_y, False])
                
            # 벽이 없는 곳으로 움직일 때 -> 정상적으로 이동 처리 해준다.
            elif not graph[new_x][new_y] and not visited[new_x][new_y][one_punch]:
                visited[new_x][new_y][one_punch] = visited[x][y][one_punch] + 1
                q.append([new_x, new_y, one_punch])
                
    return -1
    
# N, M : 가로, 세로
N, M = map(int , input().split())

graph = []

# x, y 좌표 입력
for i in range(N):
    str = input()
    str_list = list(map(int, str))
    graph.append(str_list)

# 방문값 저장 리스트
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

# 벽을 부술 수 있는 횟수, 1번
visited[0][0][True] = 1

ans = bfs(0, 0)

# 마지막까지 잘 도착하였다면 출력
if ans != 0:
    print(ans)
else:
    print(-1)
