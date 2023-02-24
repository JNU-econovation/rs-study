n,m,k = input().split()
n = int(n) # list 개수
m = int(m) # 최대 더할 수 있는 개수
k = int(k) # 반복 개수
ilist = list(map(int,input().split()))
ilist.sort(reverse=True)


print((ilist[0]*k+ilist[1])*(m // (k+1)) +ilist[1]*(m % (k+1)))

