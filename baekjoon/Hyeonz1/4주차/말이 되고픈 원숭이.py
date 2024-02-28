from collections import deque

# 입력
k = map(int, input())
w, h = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(h)]

# 다음 이동할 수 있는 노드
# 원숭이의 움직임. 상하좌우.
dw_monkey = [0, 0, -1, 1]
dh_monkey = [-1, 1, 0, 0]
# 말의 움직임. 11시부터 시계방향으로. k번만 이용 가능.
dw_horse = [-2, -1, 1, 2, 2, 1, -1, -2]
dh_horse = [1, 2, 2, 1, -1, -2, -2, -1]
