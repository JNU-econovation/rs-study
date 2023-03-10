# N : 어떤 수, K : 어떤 수를 나눌 수, cnt : 전체 과정 실행 횟수
N, K = map(int, input().split())

cnt = 0

while N != 1:
    if N % K == 0:
        N = N // K
        cnt += 1
    else:
        N -= 1
        cnt += 1

print(cnt)