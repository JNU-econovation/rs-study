# N : 세로 크기, K : 가로 크기, player_x : 유저 x 좌표, player_y : 유저 y 좌표, player_d : 유저 방향
# dx : x 선상에서 동서남북 이동 값, dy : y 선상에서 동서남북 이동 값, cnt : 캐릭터가 방문한 칸 수, no_place : 주위 1인 공간 수
N, M = map(int, input().split())

player_x, player_y, player_d = map(int, input().split())

map_list = [[]]

for i in range(N):
    col = list(map(int, input().split()))
    map_list.append(col)

# 동, 서, 남, 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 현재 방향을 기준으로 왼쪽 방향으로 90도 턴
def turn_left_90d(player_d):
    # 동 -> 북
    if player_d == 1:
        player_d = 0
    # 서 -> 남
    elif player_d == 3:
        player_d = 2 
    # 남 -> 동
    elif player_d == 2:
        player_d = 1
    # 북 -> 서
    elif player_d == 0:
        player_d = 3
    
cnt = 1
no_place = 0
map_list[player_x][player_y] = 1


while True:
    # 1. 왼쪽 방향으로 턴 ex) 턴한 후 이동할 x 좌표 = 기존 x 좌표 + 턴한 방향에 따른 이동 좌표
    turn_left_90d(player_d)
    new_player_x = player_x + dx[player_d]
    new_player_y = player_y + dy[player_d]
    
    # 2. 턴하고, 정면에 가보지 않은 칸 있으면 이동
    if map_list[new_player_x][new_player_y] == 0:
        map_list[new_player_x][new_player_y] = 1
        player_x = new_player_x
        player_y = new_player_y
        cnt += 1
        no_place = 0
        continue
    # 해당 정면이 막혀있다면 1단계로 돌아가서, 제자리에서 돌면서 막히지 않는 곳을 살핀다.
    else:
        no_place += 1

    # 3. 모든 칸들이 다 막혀있다면 뒤로 한 칸 이동해라
    if no_place == 4:
        new_player_x = player_x - dx[player_d]
        new_player_y = player_y - dy[player_d]

        # 만약 뒤로 이동한 한칸의 공간이 있었다면 뒤로 가고 1단계로 돌아간다. 
        if map_list[new_player_x][new_player_y] == 0:
            player_x = new_player_x
            player_y = new_player_y
    
            # 다 막혀있고, 뒤로 이동할 수도 없다면 멈춰라
        else:
            break
    
        no_place = 0
    
print(cnt)