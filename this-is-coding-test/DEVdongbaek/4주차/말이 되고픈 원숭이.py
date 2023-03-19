from collections import deque

# 말은 장애물을 뛰어 넘고, 현재 좌표 기준 [x+-2][y+-1] or [x+-1][y+-2] 이동 가능
# 킹숭이는 K 번은 그렇게 이동 가능, K번이 지난 후 부터는 상하좌우만 가능
# for문을 k번 이내로 돌려야 하겠네
# 단순 이동 문제가 아닌 스킬이 부여된 문제에서는 3차원 배열을 사용하는 게 좋아보이네
# 스킬 정보는 3차원에 저장시키기

# (-1, -2), (-2, -1), (2, -1), (1, -2), (-2, 1), (-1, 2), (2, 1), (1, 2)
horse_dx = [-1, -2, +2, +1, -2, -1, +2, +1]
horse_dy = [-2, -1, -1, -2, +1, +2, +1, +2]

# 상, 하, 좌, 우
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

def bfs(cnt):
    
    q = deque()

    # x, y 좌표
    q.append((0, 0, cnt))
    
    while q:

        x, y, K = q.popleft()

        if x == H - 1 and y == W - 1:
            return visited[x][y][K]
        
        # 아직 말을 흉내낼 수 있다면
        # 말처럼 이동
        if K > 0:      
            for i in range(8):                
                new_x = x + horse_dx[i]
                new_y = y + horse_dy[i]

                if new_x < 0 or new_x >= H or new_y < 0 or new_y >= W:
                    continue

                # 아직 방문하지 않았고, 이동할 수 있는 평지일 때
                if graph[new_x][new_y] == 0 and visited[new_x][new_y][K-1] == 0:
                    visited[new_x][new_y][K-1] = visited[x][y][K] + 1
                    q.append((new_x, new_y, K-1))

        # 이제 킹숭이 힘으로
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x < 0 or new_x >= H or new_y < 0 or new_y >= W:
                continue

            # 아직 방문하지 않았고, 이동할 수 있는 평지일 때
            if graph[new_x][new_y] == 0 and visited[new_x][new_y][K] == 0:
                visited[new_x][new_y][K] = visited[x][y][K] + 1
                q.append((new_x, new_y, K))
    
    # while문 로직에서 return을 거치지 않았다면 해당 return 실행
    # 즉 끝까지 이동하지 못했다면 -1 출력
    return -1

K = int(input())

W, H = map(int, input().split())

graph = []

# x, y 좌표 입력
for i in range(H):
    graph.append(list(map(int, input().split())))

# graph -> 장애물 파악, visited -> 방문 값 누적과 말 이동횟수
# 만약 K -> 스킬의 갯수가 많으면 3차원 배열이 많음
visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]

ans = bfs(K)

print(visited)
print(ans)
