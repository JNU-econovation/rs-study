N = int(input())
arr = [list(map(str, input())) for _ in range(N)]
dx = [1, 0, -1, 0]  # x의 이동에 따른 y의 이동
dy = [0, 1, 0, -1]
normal_count = 0
juck_count = 0


def bfs(q, visited, a, b):
    color = arr[a][b]
    visited[a][b] = True
    q.append((a, b))   # 큐에 (a,b) 튜플로 넣기.
    while q:  # q에 값이 없어질때까지
        # 현재 q에서 첫번째 있는거 , 그 노드와 연결된 노드들 모두 돌기 위해 첫 노드 고르기, 그 해당 번호 빼기.
        cur = q.pop(0)
        for i in range(4):   # 상하좌우로 이동가능하므로 4번
            nx = cur[1]+dx[i]  # 현재 위치의 x좌표에서 이동하는 방법 4가지 시행
            ny = cur[0]+dy[i]  # 현재 위치의 y좌표에서 이동하는 방법 4가지 시행
            # 예외
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if arr[ny][nx] != color or visited[ny][nx] == True:
                continue
            else:
                q.append((ny, nx))
                visited[ny][nx] = True


def checking(q, visited):
    count = 0
    for i in range(N):
        for j in range(N):
            if (visited[i][j] == False):
                bfs(q, visited, i, j)
                count += 1

    return count


q = list()
visited = [[False] * N for _ in range(N)]
normal_count = checking(q, visited)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'
q2 = list()
visited2 = [[False] * N for _ in range(N)]
juck_count = checking(q2, visited2)

print(normal_count, juck_count)
