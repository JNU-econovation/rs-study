# 적록색약 X
from collections import deque

# 입력
n = int(input())
painting = [list(map(str, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
total_red = 0
total_blue = 0
total_green = 0
total_rg = 0

# 상하좌우
    # 다음 방문 노드 만들기
dcol = [-1, 1, 0, 0]
drow = [0, 0, -1, 1]


# bfs 함수 정의
    # 입력받은 색깔을 탐색하여 구역값을 올리는 함수
def bfs_normal(painting, col, row, visited, color, cnt):
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
            # 노드가 painting을 벗어나는지 확인
            if  ncol >= 0 and ncol < n and nrow >= 0 and nrow < n:
                # 이전 방문 이력이 없고, 입력받은 색상에 해당하는 노드를 방문
                if painting[ncol][nrow] == color and not visited[ncol][nrow]:
                    visited[ncol][nrow] = True
                    queue.append([ncol, nrow])

    return cnt + 1

def bfs_weakness(painting, col, row, visited, cnt):
    queue = deque()
    queue.append([col, row])
    visited[col][row] = False

    while queue:
        v = queue.popleft()
        col, row = v[0], v[1]

        for i in range(4):
            # 다음 방문 노드 만들기
            ncol = col + dcol[i]
            nrow = row + drow[i]
            # 노드가 painting을 벗어나는지 확인
            if  ncol >= 0 and ncol < n and nrow >= 0 and nrow < n:
                # 이전 방문 이력이 없고, 입력받은 색상에 해당하는 노드를 방문
                if (painting[ncol][nrow] == "R" or painting[ncol][nrow] == "G") and visited[ncol][nrow]:
                    visited[ncol][nrow] = False
                    queue.append([ncol, nrow])

    return cnt + 1

for colum in range(n):
    for row in range(n):
        if not visited[colum][row] and painting[colum][row] == "R":
            total_red = bfs_normal(painting, colum, row, visited, "R", total_red)
        elif not visited[colum][row] and painting[colum][row] == "G":
            total_green = bfs_normal(painting, colum, row, visited, "G", total_green)
        elif not visited[colum][row] and painting[colum][row] == "B":
            total_blue = bfs_normal(painting, colum, row, visited, "B", total_blue)

for colum in range(n):
    for row in range(n):
        if visited[colum][row] and painting[colum][row] == "R":
            total_rg = bfs_weakness(painting, colum, row, visited, total_rg)

print(total_red + total_blue + total_green, end = ' ')
print(total_rg, total_blue)
