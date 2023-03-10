# coordinate : 나이트 위치, col_dict : 문자 열번호를 숫자로 저장한 딕셔너리, move_list : 나이트가 움직일 수 있는 경우의 수
coordinate = input()

row = int(coordinate[1])

col_dict = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8}

col = col_dict.get(coordinate[0])

move_list = [[-2, 1], [-2, -1], [2, -1], [2, 1], [1, -2], [1, 2], [-1, -2], [-1, 2]]

ans = 0

for move in move_list:
    if row + move[0] >= 1 and row + move[0] <= 8:
        if col + move[1] >= 1 and col + move[1] <= 8:
            ans += 1


print(ans)