a = int(input())
n = 1
sum = n*(n+1)/2

# sum에 1, 2, 3...을 계속 더해나가야 한다. => 몇까지 더해야 할까?
# sum이 a보다 커지면 더하는 작업을 멈춘다.
# a와 n의 관계식을 알아야 하나?
# sum = n*(n+1)/2
# n*(n+1)/2 < a
while a > sum:
    n += 1
    sum = n*(n+1)/2

print(n)