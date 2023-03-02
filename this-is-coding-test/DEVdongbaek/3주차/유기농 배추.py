from collections import deque
    
def bfs(x, y):
    
    q = deque()
    q.append((x, y))
    
    # 방문 처리
    graph[x][y] = 0
    
    while q:
        
        x, y = q.popleft()

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
                continue 
            
            if graph[new_x][new_y] == 1:
                graph[new_x][new_y] = 0
                q.append((new_x, new_y))
    
    # return은 값을 반환하는 기능뿐만 아니라 함수 중간에서 바로 빠져나오는 기능도 있습니다.
    return

# T : 테스트 케이스 개수
T = int(input())

for _ in range(T):
    # N, M : 배추밭의 가로, 세로 길이, K : 배추 갯수
    N, M, K = map(int , input().split())

    # 배추 x, y 좌표
    graph = [[0]*M for _ in range(N)]

    print(graph)

    for i in range(K):
        x, y = map(int , input().split())
        graph[x][y] = 1

    print(graph)

    # 상, 하, 좌, 우
    dx = [-1, +1, 0, 0]
    dy = [0, 0, -1, +1]                
    ans = 0     
    for i in range(N):
        for j in range(M):
            # 배추가 있는 땅이면
            if graph[i][j] == 1:
                # 근처에 있는 땅들을 모두 들려서 0 처리하고, 1 더함
                bfs(i, j)
                ans += 1
                
    print(ans)
    