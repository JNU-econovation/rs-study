N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(M)]  # N은 x축, M 은 y축
opp = 1    # 부수는 기회 1번
q=[]
visited=[]
dx=[-1,1,0,0]
dy=[0,0,1,-1]
# 갈 수 있는 곳이 없을 경우 , -> 

def bfs(q, visited, a, b):
    visited[a][b] = True
    q.append((a, b))   # 큐에 (a,b) 튜플로 넣기.
    while q:  # q에 값이 없어질때까지
        # 현재 q에서 첫번째 있는거 , 그 노드와 연결된 노드들 모두 돌기 위해 첫 노드 고르기, 그 해당 번호 빼기.
        cur = q.pop(0)
        for i in range(4):   # 상하좌우로 이동가능하므로 4번
            nx = cur[1]+dx[i]  # 현재 위치의 x좌표에서 이동하는 방법 4가지 시행
            ny = cur[0]+dy[i]  # 현재 위치의 y좌표에서 이동하는 방법 4가지 시행
            
            if nx>=0 and ny>=0 and ny<M and nx<N:
                if arr[nx][ny]==0:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                     # nx ny 가 0이상, N,M 이하여야 함.  arr[nx] arr[ny] 는 0이어야함. 
                     # 근데 1 이고 , 그다음에 0 이면, 그리고 opp 이 1 이면 뚫을 수 있음.
                elif arr[nx][ny]==1 and opp==1:
                    

def checking(array, q, visited):  # 전부 돌아보며 bfs 한 후 한묶음으로된 노드들의 개수를 반환하는함수
    count = 0
    for i in range(N):
        for j in range(M):
            if (visited[i][j] == False) and (array[i][j] == 1):
                bfs(q, visited, i, j)
                count += 1
    return count
           

            
          
