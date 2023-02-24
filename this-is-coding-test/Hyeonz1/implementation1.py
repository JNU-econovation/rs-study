# 조건
    # 1. 8 x 8 평면
    # 2. 나이트의 이동 형태
# 입력
    # 나이트의 위치
# 출력
    # 나이트 이동 경우의 수

# 나이트 위치마다 이동 경우의 수를 구하고 위치를 입력받은 후에 switch문을 이용하여 경우의 수를 출력한다.
    # python에서는 switch-case문이 없다. 대안으로 dictionary를 사용하라.
    # 64가지 경우를 모두 dictionary 자료형으로 작성한다. => 개선이 필요

coordination = input()

# 1. 위 두 칸이 있는지 확인
    # 2. 있다면 두 칸 위에서 좌, 우로 이동이 가능한지 확인
        # 3. 이동 가능한 만큼 counter++
    # 2. 없다면 다른 방향 탐색
# 4. 4방향에 대해서 위의 과정을 반복 수행

# 위 두 칸이 있는지 확인 => 처음 좌표가 3~8행이면 위 두 칸이 있다.
# 방향별 확인 조건
    # 위 두 칸이 있는가? => 3~8행
        # 좌로 이동 가능한가? => b~h열
        # 우로 이동 가능한가? => a~g열
    # 오른쪽 두 칸이 있는가? => a~f열
        # 위로 이동 가능한가? => 2~8행
        # 아래로 이동 가능한가? => 1~7행
    # 아래 두 칸이 있는가? => 1~6행
    # 왼쪽 두 칸이 있는가? => c~h열

column = ord(coordination[0])
row = int(coordination[1])
counter = 0

if(row >= 3 and row <= 6):
    if(column == 97 or column == 104):
        counter += 2
    else:
        counter += 4
else:
    if(column == 97 or column == 104):
        counter += 1
    else:
        counter += 2

if(column >= 99 and column <= 102):
    if(row == 1 or row == 8):
        counter += 2
    else:
        counter += 4
else:
    if(row == 1 or row == 8):
        counter += 1
    else:
        counter += 2


print(counter)
