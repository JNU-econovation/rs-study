
N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(M)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = list()
visited = [[False] * N for _ in range(M)]
count = 0


def bfs(a, b, count):
    visited[a][b] = True
    q.append((a, b))   # 큐에 (a,b) 튜플로 넣기.
    count += 1
    while q:  # q에 값이 없어질때까지
        # 현재 q에서 첫번째 있는거 , 그 노드와 연결된 노드들 모두 돌기 위해 첫 노드 고르기, 그 해당 번호 빼기.
        cur = q.pop(0)
        for i in range(4):   # 상하좌우로 이동가능하므로 4번
            nx = cur[1]+dx[i]  # 현재 위치의 x좌표에서 이동하는 방법 4가지 시행
            ny = cur[0]+dy[i]  # 현재 위치의 y좌표에서 이동하는 방법 4가지 시행
            # 못 가는 경우(모서리에 있거나 칸막이 존재하는 경우)
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if maze[ny][nx] == 0 or visited[ny][nx] == True:
                continue
            else:
                q.append((nx, ny))
                visited[ny][nx] = True
                count += 1
    return count


print(bfs(0, 0, count))

# 2차원 배열 입력받구요
# dx, dy (x와 y의 이동 방법)
# 큐 선언 후, 모든 노드들 방문 False로 선언해줍니다.
# 함수 두개 선언해주기
# 첫번째는 해당 노드에 방문 후(방문 True 로 해주기) 큐에 넣고, 큐에 넣어져 있는 곳 상하좌우로 이동할 수 있으면 이동.
#            이동한다면, 큐에 해당 노드 넣은후 큐가 없어질때까지 반복문 돌아주기(이때 이동할 곳 없어지면, 즉 노드 끝나면 종료)
#    ---> BFS 하는 함수
# 두번째 함수는 노드들을 전부 돌고,.,, 갈 수 있고, 방문 안한곳이면 위에 함수 호출.
#    ----> 모든 노드를 도는 함수


# 3 3
# 1 1 0
# 0 1 0
# 0 1 1
# ->5
