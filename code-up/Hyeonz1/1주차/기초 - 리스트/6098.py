cheeseMap = [list(map(int, input().split())) for _ in range(10)]

# 개미는 (2,2)에서 움직이기 시작한다.
# 개미는 (2,3),(2,4)..로 나아가다가 (2, y)가 1인 지점에서 (3, y-1)로 이동한다.
# 다음 이동 칸이 2이면 stop한다.

# 개미가 오른쪽으로 움직이는 조건: 현재 위치 position = [x, y]라고 했을 때, [x, y + 1] == 0인 경우
# 개미가 아래쪽으로 움직이는 조건: 현재 위치 position[x][y]라고 했을 때, position[x][y + 1] == 1인 경우
# 개미가 멈추는 조건: 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우
    # 1. position[x][y + 1] == 1 and position[x + 1][y] == 1
    # 2. position[x][y]에서 x == 8, y == 8인 경우
    # 3. position[x][y] == 2

cp = [1, 1] # cp[0]: 현재 개미 x좌표, cp[1]: 현재 개미 y좌표, position[cp[0]][cp[1]]
cheeseMap[cp[0]][cp[1]] = 9
# 1. 벽에 부딪히기 전까지 오른쪽으로 움직인다.
# 2. 오른쪽에 벽이 안나올 때까지 아래로 이동한다.
# 1, 2번을 멈추는 조건을 만족하기 전까지 반복한다.

while cheeseMap[cp[0]][cp[1]] != cheeseMap[8][8] and (cheeseMap[cp[0] + 1][cp[1]] != 1 or cheeseMap[cp[0]][cp[1] + 1] != 1) and cheeseMap[cp[0] + 1][cp[1]] == 2 and cheeseMap[cp[0]][cp[1] + 1] == 2:
    for y in range(7):
        if cheeseMap[cp[0]][cp[1] + y] == 1:
            break
        else:
            cheeseMap[cp[0]][cp[1] + y] == 9
            cp[1] += 1
    
    for x in range(7):
        if cheeseMap[cp[0]][cp[1] + 1] == 0:
            break
        else:
            cheeseMap[cp[0] + x][cp[1]] == 9
            cp[0] += 1

for i in range(len(cheeseMap)):
    for j in range(len(cheeseMap[i])):
        print(cheeseMap[i][j], end = " ")
    print("")


