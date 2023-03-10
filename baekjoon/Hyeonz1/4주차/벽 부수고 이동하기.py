from collections import deque

# 입력받기 및 초기화
n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
broken = False 

# 상하좌우
    # 다음 방문 노드 만드는데 이용
dcol = [-1, 1, 0, 0]
drow = [0, 0, -1, 1]

# bfs 함수 정의
def bfs(col, row):
    global map, visited, broken
    queue = deque()
    queue.append([col,row])

    while queue:
        col, row = queue.popleft()

        for i in range(4):
            ncol = col + dcol[i]
            nrow = row + drow[i]
        
        if ncol < 0 or ncol > n or nrow < 0 or nrow > m:
            continue

        if map[ncol][nrow] == 1 and broken == True:
            continue
        
        if map[col][row] == 1 and broken == False:
            broken = True
            map[ncol][nrow] = map[col][row] + 1

        if map[ncol][nrow] == 0:
            map[ncol][nrow] = map[col][row] + 1
            queue.append([ncol, nrow])

    return map[n - 1][m - 1]

# 조건
    # 벽을 한 개까지 부술 수 있다!
        # broken이라는 변수를 두고 broken == False이면 부숴도 되고, broken == True이면 더 이상 벽을 부수지 않도록 한다.
        # 다음 노드를 탐색할 때, broken == False이고, 
    # n, m까지 가는게 불간으하면 -1을 출력한다.
# 출력
print(bfs(0, 0))