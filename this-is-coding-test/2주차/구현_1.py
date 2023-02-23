# 구현이란 머릿속의 알고리즘을 소스코드로 바꾸는 과정.
# 완전탐색: 모든 경우의 수 다 계산  , 시뮬레이션 : 알고리즘 한단계씩 차례대로 수행

# 상하좌우
N = int(input())
go_list = list(map(str,input().split()))
start_X=1
start_Y=1

for i in range(len(go_list)):
    if go_list[i]=='R' and start_X<N:
        start_X+=1
    elif go_list[i]=='L' and start_X>1:
        start_X-=1
    elif go_list[i]=="U" and start_Y>1:
        start_Y -= 1
    elif go_list[i] == 'D' and start_Y<N:
        start_Y+=1

print(start_Y,start_X)
