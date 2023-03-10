# N : 행의 개수, M : 열의 개수, num_list : 입력 받은 숫자 카드들, min_list : 각 행들 중 최솟값들
N, M = map(int, input().split())

num_list = []

for i in range(N):
    num_list.append(list(map(int, input().split())))

min_list = []

for i in num_list:
    min_list.append(min(i))
    
print(max(min_list))