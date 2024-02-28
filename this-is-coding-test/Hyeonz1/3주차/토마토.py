# 토마토
from collections import deque

# 입력
m, n, h = map(int, input().split())
tomato_input = [list(map(int, input().split())) for _ in range(n * h)]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]
print(visited)
# 3차원 토마토 박스 만들기
tomato_box = [[[0]*m  for _ in range(n)] for _ in range(h)]
for row in range(m):
    for col in range(n):
        for height in range(h):
            tomato_box[height][col][row] = tomato_input[col + n * height][row]

# 다음 방문 노드 만들기
    # 뒤 좌 앞 우 상 하
dcol = [-1, 0, 1, 0, 0, 0]
drow = [0, -1, 0, 1, 0, 0]
dht = [0, 0, 0, 0, -1, 1]

# 탐색
for height in range(h):
    for col in range(n):
        for row in range(m):
            # 탐색 수행
            # 익은 토마토가 들어있는 노드부터 방문하기 시작
            print("m")

# 출력


# bfs함수 정의
def bfs(tomato_box, height, col, row, visited):
    queue = deque()
    queue.append([height, col, row])
    visited[height][col][row] = True

    while queue:
        v = queue.popleft()
        height, col, row = v[0], v[1], v[2]

        for i in range(4):
            # 다음 방문 노드 만들기
            ncol = col + dcol[i]
            nrow = row + drow[i]
            nht = height + dht[i]

            # 노드가 tomato_box를 벗어나는지 확인
            if  ncol >= 0 and ncol < n and nrow >= 0 and nrow < m and nht >= 0 and nht < h:
                # 이전 방문 이력이 없고, 0인 노드를 방문
                if tomato_box[ncol][nrow] == 0 and not visited[ncol][nrow]:
                    visited[ncol][nrow] = True
                    queue.append([ncol, nrow])
                elif tomato_box[ncol][nrow] == 1 and not visited[ncol][nrow]:
                    visited[ncol][nrow] = True


    return total_ice + 1
