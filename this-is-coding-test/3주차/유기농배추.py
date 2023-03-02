

dx = [1, 0, -1, 0]  # x의 이동에 따른 y의 이동
dy = [0, 1, 0, -1]


def bfs(array, q, visited, a, b):
    visited[a][b] = True
    q.append((a, b))   # 큐에 (a,b) 튜플로 넣기.
    while q:  # q에 값이 없어질때까지
        # 현재 q에서 첫번째 있는거 , 그 노드와 연결된 노드들 모두 돌기 위해 첫 노드 고르기, 그 해당 번호 빼기.
        cur = q.pop(0)
        for i in range(4):   # 상하좌우로 이동가능하므로 4번
            nx = cur[1]+dx[i]  # 현재 위치의 x좌표에서 이동하는 방법 4가지 시행
            ny = cur[0]+dy[i]  # 현재 위치의 y좌표에서 이동하는 방법 4가지 시행
            # 못 가는 경우(모서리에 있거나 칸막이 존재하는 경우)
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if array[ny][nx] == 0 or visited[ny][nx] == True:
                continue
            else:
                q.append((ny, nx))
                visited[ny][nx] = True


def checking(array, q, visited):  # 전부 돌아보며 bfs 한 후 한묶음으로된 노드들의 개수를 반환하는함수
    count = 0
    for i in range(N):
        for j in range(M):
            if (visited[i][j] == False) and (array[i][j] == 1):
                bfs(array, q, visited, i, j)
                count += 1
    return count


test_num = int(input())
for _ in range(test_num):

    N, M, cabbage = map(int, input().split())
    array = [[0 for _ in range(M)] for _ in range(N)]    # 밭의 모든 요소를 0으로 만들기

    q = list()
    visited = [[False] * M for _ in range(N)]

    for _ in range(cabbage):    # 배추가 있는 부분을 1로 바꾸기
        x, y = map(int, input().split())
        array[x][y] = 1

    # 테스트를 여러번 할 수도 있으므로 로컬변수로 선언해주고, 함수호출할때 각각 넣어주게 한다.
    print(checking(array, q, visited))
