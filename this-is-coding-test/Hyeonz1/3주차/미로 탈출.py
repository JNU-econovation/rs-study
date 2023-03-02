# 미로 탈출 O
from collections import deque

# 입력 받기와 초기화
n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
movement = 0


# 상하좌우
    # 다음 방문 노드 만들기
dcol = [-1, 1, 0, 0]
drow = [0, 0, -1, 1]
            
# bfs 함수 정의
def bfs(maze, col, row, visited):
    global movement
    queue = deque()
    queue.append([col, row])
    visited[col][row] = True

    while queue:
        v = queue.popleft()
        col, row = v[0], v[1]
        movement += 1
        print(col,row)
        if col == n - 1 and row == m - 1:
            queue.clear()
            break
        cnt = 0

        for i in range(4):
            # 다음 방문 노드 만들기
            ncol = col + dcol[i]
            nrow = row + drow[i]
            # 노드가 maze를 벗어나는지 확인
            if  ncol >= 0 and ncol < n and nrow >= 0 and nrow < m:
                # 이전 방문 이력이 없고, 1인 노드를 방문
                if maze[ncol][nrow] == 1 and not visited[ncol][nrow]:
                    visited[ncol][nrow] = True
                    queue.append([ncol, nrow])
                else:
                    cnt += 1
            else:
                cnt += 1
        if cnt == 4:
            movement -= 1 # 다음번에 방문할 노드가 없으면서, 마지막 노드가 아니면 movement -= 1
            print("빠진노드", col, row)
    return 0

bfs(maze, 0, 0, visited)
print(movement)
