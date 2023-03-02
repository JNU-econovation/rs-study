# 큰 수의 법칙
# 배열 수들을 m번 더해 가장 큰 수를 만드는 법칙. 연속해서 k번 초과하여 더할 수 없다.

n, m, k = input().split()
arr = list(map(int, input().split()))
arr.sort(reverse=True)  # 오름차순으로 정렬해주기

# 가장 앞 수를 k번 더하기.
num=0
for i in range(1,int(m)+1):   # 1부터  m까지
    if i%(int(k)+1)==0:  # i 가 k+1의 배수마다 두번째로 큰 수 더하기(k번째까지는 0번째 더하고 다음번째만 1번째 더해야돼서)
        num+=arr[1]
    else:
        num+=arr[0]

print(num)


