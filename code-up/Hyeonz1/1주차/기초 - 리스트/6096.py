# 입력1. 2차원 배열
coordinate = [list(map(int, input().split())) for _ in range(19)]

# 입력2. 뒤집기 횟수
count = int(input())

# 입력3. 뒤집기 좌표
condition = [list(map(int, input().split())) for _ in range(count)]

# 작업 : 좌표에 해당하는 가로줄과 세로줄의 값을 반전시켜야 한다.
# 1. 좌표를 가져온다.
    # condition[i][j]에서
    # j가 0일 때, 가로줄 반전
    # j가 1일 때, 세로줄 반전

# 2. 좌표에 해당하는 줄의 값을 반전시킨다.
    # 가로줄의 반전. 
    # 세로줄의 반전.
for i in range(2):
    for j in range(len(condition)):
        if (i == 0): # 가로줄 반전. 가로값 고정
            for x in range(19):
                if(coordinate[condition[j][i] - 1][x] == 0):
                    coordinate[condition[j][i] - 1][x] = 1
                else:
                    coordinate[condition[j][i] - 1][x] = 0
        else:
            for y in range(19): # 세로줄 반전. 세로값 고정
                if (coordinate[y][condition[j][i] - 1] == 0):
                    coordinate[y][condition[j][i] - 1] = 1
                else:
                    coordinate[y][condition[j][i] - 1] = 0

        
for i in range(len(coordinate)):
    for j in range(len(coordinate[i])):
        print(coordinate[i][j], end = " ")
    print("")