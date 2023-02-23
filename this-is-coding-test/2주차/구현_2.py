# 시각
N = int(input())
h=0
m=0
s=0
count=0
N= (N+1)*60*60
def find_three(p):
    if  p==3 or p%10==3 or p//10==3:
        return True
    else:
        return False


for _ in range(N):
    if find_three(h) or find_three(m) or find_three(s):
        count+=1
    if h==N and m==59 and s==59:
        break
    elif s>58 and m>58:
        h+=1
        s=0
        m=0
    elif s>58:
        m+=1
        s=0
    else:
        s+=1

print(count)

# if '3' in str(s) + str(h) + str(m) 를 이용하자...