# 유기농 배추 O
from collections import deque

# bfs 함수 정의
# 상하좌우
    # 다음 방문 노드 만들기
dcol = [-1, 1, 0, 0]
drow = [0, 0, -1, 1]

def bfs(cabbage_map, col, row, visited):
    queue = deque()
    queue.append([col, row])
    visited[col][row] = True

    while queue:
        v = queue.popleft()
        col, row = v[0], v[1]

        for i in range(4):
            # 다음 방문 노드 만들기
            ncol = col + dcol[i]
            nrow = row + drow[i]
            # 노드가 cabbage_map를 벗어나는지 확인
            if  ncol >= 0 and ncol < n and nrow >= 0 and nrow < m:
                # 이전 방문 이력이 없고, 1인 노드를 방문
                if cabbage_map[ncol][nrow] == 1 and not visited[ncol][nrow]:
                    visited[ncol][nrow] = True
                    queue.append([ncol, nrow])
                elif cabbage_map[ncol][nrow] == 0 and not visited[ncol][nrow]:
                    visited[ncol][nrow] = True


    return total_warm + 1

# 입력 및 초기화
t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    coordinate = [list(map(int, input().split())) for _ in range(k)]
    visited = [[False] * m for _ in range(n)]

        # cabbage_map을 만들어주기
    cabbage_map = [[0] * m for _ in range(n)]

    for col in range(k):
        cabbage_map[coordinate[col][1]][coordinate[col][0]] = 1

    total_warm = 0



    for colum in range(n):
        for row in range(m):
            if not visited[colum][row] and cabbage_map[colum][row] == 1:
                total_warm = bfs(cabbage_map, colum, row, visited)

    print(total_warm)

