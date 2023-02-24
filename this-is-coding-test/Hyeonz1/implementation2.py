n, m = map(int, input().split())
x, y, d = map(int, input().split())
my_map = [list(map(int, input().split())) for _ in range(m)]

# 1. 현재 방향을 기준으로 왼쪽 방향으로 돈다.
    # 2. 정면이 가보지 않은 육지라면 해당 위치로 이동한다.
        # 3. 새로운 위치에 대해 1번부터 다시 작업을 수행한다.
    # 2. 아니라면 다른 방향에 대해서 위의 과정을 수행한다.
# 3. 한 바퀴를 돌 때까지 캐릭터의 이동이 일어나지 않았다면, 뒤로 갈 수 있는지 판단한다.
    # 4. 갈 수 있으면 간다. 그리고 새로운 위치에 대해 1번부터 다시 작업을 수행한다.
    # 4. 갈 수 없으면 종료.

character_direction = [0, 1, 2, 3]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
movement = 0
cur_x, cur_y = x, y

my_map[x][y] = 2
# 1단계로 돌아가는 경우 
    # 1. 전진한 경우
    # 2. 왼쪽에 갈 수 있는 칸이 없는 경우
    # 3. 네 방향 모두 갈 수 없는 칸인 경우
while cur_x == x and cur_y == y:

    print("1단계 실행")
    for i in range(4):
        print("현재위치 %d %d" %(x, y))
        d = character_direction[d - 1]

        if(my_map[x + dx[d]][y + dy[d]] == 0):
            print(x, y)
            x = x + dx[d]
            y = y + dy[d]
            my_map[x + dx[d]][y + dy[d]] = 2
            movement += 1
            print("전진")
            break
        else:
            print("전진불가")
            continue

    if(cur_x == x and cur_y == y):
        print("움직일 수 없다!")
        if(my_map[x + dx[character_direction[d-2]]][y + dy[character_direction[d-2]]] == 2):
            print("뒤로 한 칸 이동")
            x = x + dx[character_direction[d-2]]
            y = y + dy[character_direction[d-2]]
            movement += 1
            cur_x, cur_y = x, y
        else:
            print("뒤로도 이동 불가 - END")
            print(movement)
            break
    else:
        cur_x, cur_y = x, y
