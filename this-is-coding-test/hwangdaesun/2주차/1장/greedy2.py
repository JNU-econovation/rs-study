n,m = input().split()
n = int(n)
m = int(m)

ilist = [list(map(int, input().split())) for _ in range(n)]

minlist = []


for n in range(n):
    minlist.append(min(ilist[n]))

print(minlist)
minlist.sort(reverse=True)
print(minlist[0])


# 문법 사용한 것
# list에서 최소를 구할 때는 min()함수를 사용!
# 입력으로 받는 이중 리스트 -> [list(map(int,input().split())) for _ in range(m)]

# n,m이 행과 열인 것이 x,y좌표와 반대여서 배열을 활용하는 데 헷갈렸다.

