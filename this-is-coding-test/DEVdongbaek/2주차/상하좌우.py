# N : 행의 개수, move_list : 입력 받은 행동들, x, y : x, y 좌표
N = int(input())

move_list = list(input().split())

x, y = 0, 0

for i in range(len(move_list)):
    move_str = move_list[i]
    if move_str == "L":
        if x > 0:
            x -= 1
        
    elif move_str == "R":
        if x < 4:
            x += 1

    elif move_str == "U":
        if y > 0:
            y -= 1

    else:
        if y < 4:
            y += 1

print(x, y)