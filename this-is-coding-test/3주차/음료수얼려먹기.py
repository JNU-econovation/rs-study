
N, M = map(int, input().split())
ice_mold = [list(map(int, input().split())) for _ in range(M)]

dx = [1, 0, -1, 0]  # x의 이동에 따른 y의 이동
dy = [0, 1, 0, -1]

q = list()
visited = [[False] * N for _ in range(M)]
count = 0


def bfs(a, b):
    visited[a][b] = True
    q.append((a, b))   # 큐에 (a,b) 튜플로 넣기.
    while q:  # q에 값이 없어질때까지
        # 현재 q에서 첫번째 있는거 , 그 노드와 연결된 노드들 모두 돌기 위해 첫 노드 고르기, 그 해당 번호 빼기.
        cur = q.pop(0)
        for i in range(4):   # 상하좌우로 이동가능하므로 4번
            nx = cur[1]+dx[i]  # 현재 위치의 x좌표에서 이동하는 방법 4가지 시행
            ny = cur[0]+dy[i]  # 현재 위치의 y좌표에서 이동하는 방법 4가지 시행
            # 못 가는 경우(모서리에 있거나 칸막이 존재하는 경우)
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if ice_mold[ny][nx] == 1 or visited[ny][nx] == True:
                continue
            else:
                q.append((ny, nx))
                visited[ny][nx] = True


for i in range(M):   # ice_mold 의 모든 부분을 돌기
    for j in range(N):
        if (visited[i][j] == False) and (ice_mold[i][j] == 0):
            bfs(i, j)
            count += 1


print(count)

# test 한거
# 4 4
# 0 0 0 1
# 1 1 1 0
# 0 1 0 1
# 1 0 1 0
# -> 6 나옴

# 3 3
# 1 1 1
# 1 0 1
# 0 1 0
# -> 3 나옴.
