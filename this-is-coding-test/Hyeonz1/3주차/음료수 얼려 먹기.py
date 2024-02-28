# 음료수 얼려 먹기 O
from collections import deque

# 입력 받기
n, m = map(int, input().split())
ice_tray = [list(map(int, input().strip())) for _ in range(n)] # 입력받은 리스트 자체를 graph라고 생각한다!
visited = [[False] * m for _ in range(n)]
total_ice = 0


# 상하좌우
    # 다음 방문 노드 만들기
dcol = [-1, 1, 0, 0]
drow = [0, 0, -1, 1]


# bfs 함수 정의
def bfs(ice_tray, col, row, visited):
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
            # 노드가 ice_tray를 벗어나는지 확인
            if  ncol >= 0 and ncol < n and nrow >= 0 and nrow < m:
                # 이전 방문 이력이 없고, 0인 노드를 방문
                if ice_tray[ncol][nrow] == 0 and not visited[ncol][nrow]:
                    visited[ncol][nrow] = True
                    queue.append([ncol, nrow])
                elif ice_tray[ncol][nrow] == 1 and not visited[ncol][nrow]:
                    visited[ncol][nrow] = True


    return total_ice + 1


for colum in range(n):
    for row in range(m):
        if not visited[colum][row] and ice_tray[colum][row] == 0:
            total_ice = bfs(ice_tray, colum, row, visited)

print(total_ice)

