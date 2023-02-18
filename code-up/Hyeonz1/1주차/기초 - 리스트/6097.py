size = list(map(int, input().split()))
total = int(input())
stick = []

for i in range(total):
    stick.append(list(map(int, input().split())))

status = []

for i in range(size[0]):
    status.append([])
    for j in range(size[1]):
        status[i].append(0)

# 막대 놓기
    # stick[i][0]은 길이
    # stick[i][1]은 가로, 세로
        # 가로라면, 시작점을 기준으로 가로로 길이만큼 배치
    # stick[i][2]는 x좌표
    # stick[i][3]은 y좌표 
        # => status[stick[i][2] - 1][stick[i][3] - 1]를 시작점으로 배치

for i in range(total):
    if (stick[i][1] == 0):
        for j in range(stick[i][0]):
            status[stick[i][2] - 1][stick[i][3] - 1 + j] = 1
    else:
        for j in range(stick[i][0]):
            status[stick[i][2] - 1 + j][stick[i][3] - 1] = 1

for i in range(len(status)):
    for j in range(len(status[i])):
        print(status[i][j], end=" ")
    print("")