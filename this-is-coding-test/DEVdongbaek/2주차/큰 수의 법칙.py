# N : 배열의 크기, M : 더하는 횟수, K : 한 인덱스가 연속으로 나올 수 있는 횟수, sum : 최종 더해진 숫자, cnt : 한 숫자가 연속으로 더해진 횟수
N, M, K = map(int, input().split())

num_list = list(map(int, input().split()))

# 정렬을 사용하여서, max, max보다 작은 값 구함
num_list.sort()

sum = 0
cnt = 0

for i in range(M):
    if cnt < K-1:
        sum += num_list[N-1]
        cnt += 1
    else:
        sum += num_list[N-2]
        cnt = 0


print(sum)

