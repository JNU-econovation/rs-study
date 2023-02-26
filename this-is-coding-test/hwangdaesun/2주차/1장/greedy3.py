n,k = input().split()
n = int(n)
k = int(k)

count = 0

if(n<k):
    count += n
else:
    while(n % k != 0):
        n -=1
        count += 1
    count += (n//k)
print(count)

# n>k인 관계만 생각하고, n<k인 관계는 생각하지 못했다.

# 몫과 나머지 활용 방법??

