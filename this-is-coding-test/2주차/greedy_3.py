# 1이 될 때까지
# (n -1) 나 /(k)   를 실행할때 n 이 1이 될때까지 최소 횟수 구하기.
#  나누는것은 나누어떨어질때만 사용 가능

N, K = input().split()
num=0
N=int(N)
K=int(K)
while N!=1:
    if N%K==0:
        N=N/K
        num+=1
    else:
        N-=1
        num+=1
print(num)