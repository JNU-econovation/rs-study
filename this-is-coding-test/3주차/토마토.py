N, M, H = map(int, input().split())
# 3차원 배열 찾아보기
# 토마토 첫번째줄에는 가로세로 높이 | 두번째줄에는 토마토 한 판의 요소가 한줄씩 주어진다.(M개 씩 N줄)
# 마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다. -> bfs 도는 횟수 구하기.
# 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, -> 먼저 처음에 한번 돌아서 확인 -> 전부 1아니면 -1이면 0 출력
# 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다. -> bfs 완료 후 남아있는 0 토마토가 있는지 확인 후 있으면 -1츨력
# 1: 익 토 / 0: 안익토 / -1 : 토마토 없음.


# tomato_box 가 1 이면 익은 토마토라 넘어가야돼서 바로 큐에 추가해야함!!!!!

tomato_box = [list(map(int, input().split()))
              for _ in range(M) for _ in range(H)]
# 토마토 리스트

dx = [1, 0, -1, 0, 0, 0]  # x, y, z 이동
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0,  0, 1, -1]

q = list()
# 방문한곳
visited = [([False]*M for _ in range(N)) for _ in range(H)]

count = 0


def bfs(a, b, c):
    visited[a][b][c] = True
    q.append((a, b, c))   # 큐에 (a,b) 튜플로 넣기.
    while q:  # q에 값이 없어질때까지
        # 현재 q에서 첫번째 있는거 , 그 노드와 연결된 노드들 모두 돌기 위해 첫 노드 고르기, 그 해당 번호 빼기.
        cur = q.pop(0)
        for i in range(6):   # 상하좌우로 이동가능하므로 4번
            nx = cur[0]+dx[i]  # 현재 위치의 x좌표에서 이동하는 방법 6가지 시행
            ny = cur[1]+dy[i]  # 현재 위치의 y좌표에서 이동하는 방법 6가지 시행
            nz = cur[2]+dz[i]   # 현재 위치의 z좌표에서 이동하는 방법 6가지 시행
            # 이동 가능한경우
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and tomato_box[nx][ny][nz] == 0:
                tomato_box[nx][ny][nz] += 1
                q.append((nx, ny, nz))
                visited[nx][ny][nz] = True


for i in range(N):   # tomato_box 의 모든 부분을 돌기
    for j in range(M):
        for k in range(H):
            if data[i][j][k] == 1:
                # 높이, x,y 순서
                queue.append((i, j, k))

for i in range(N):   # tomato_box 의 모든 부분을 돌기
    for j in range(M):
        for k in range(H):
            if (visited[i][j][k] == False) and (tomato_box[i][j][k] == 0):
                bfs(i, j, k)
                count += 1


if count == 0:
    print('0')
    # bfs 를 한번도 못돌았다는 뜻이니깐 전부 익은 토마토거나 토마토 없음.

else:
    print(count)


# 1은 익은 토마토 0은 안익은 토마토 -1 은 토마토 없음.
# 만약 깊이우선탐색 중 익었거나 없으면 탐색안함.
