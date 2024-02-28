n, k = map(int, input().split())

# n이 1이 될 때까지 작업의 최소횟수
    # 작업
        # 1. n - 1
        # 2. n / k (단, 나누어 떨어질 때만 사용 가능)
    # 1이 아닌 어떤 수가 k로 주어지더라도 n을 k로 나누는 것이 n에서 1을 빼는 것보다 숫자를 더 많이 줄인다.

count = 0
while n != 1:
    if (n % k == 0):
        n //= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)
