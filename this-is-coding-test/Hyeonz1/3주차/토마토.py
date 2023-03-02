# 토마토
from collections import deque

# 입력
m, n, h = map(int, input().split())
tomato_box = [[list(map(int, input().split())) for _ in range(n)] * h]

print(tomato_box)
