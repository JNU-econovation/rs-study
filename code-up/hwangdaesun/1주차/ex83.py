a,b,c=input().split()
a = int(a)
b = int(b)
c = int(c)
number = 0
for i in range(0,a):
    for j in range(0,b):
        for k in range(0,c):
            print(i,j,k,sep=" ")
            number += 1
print(number)

# 수행 시간:1969 ms / 메모리 :27976 kb
# 개선 : number을 사용하지 말고, i*j*k