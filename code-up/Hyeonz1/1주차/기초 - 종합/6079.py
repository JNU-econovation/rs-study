# 내용 : sum이 a와 같거나 a보다 커질 때까지 sum에 이전보다 1 큰 값을 더하는 것을 반복 수행한다.
    # 1씩 커지는 변수 n이 필요.

a = int(input())
n = 0
sum = 0

while a > sum:
    n += 1
    sum += n

print(n)

# 어려웠던 점 : n값이 1씩 커지는 변수였어서 for문을 써야하는지 아닌지 헷갈렸다.
# for i in range(sum이 a보다 커졌을 때 총 더한 횟수):
#    sum += i
# 결론 : sum이 a보다 커졌을 때 총 더한 횟수를 알려면 다른 식이 한 번 더 필요하기 때문에 while문을 쓰는게 낫다.