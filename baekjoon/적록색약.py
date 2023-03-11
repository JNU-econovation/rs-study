import sys
import copy
sys.setrecursionlimit(10 ** 6)

n = int(input())
listlist1 = [list(input()) for _ in range(n)]
listlist2 = copy.deepcopy(listlist1)

for i in range(n):
    for j in range(n):
        if(listlist2[i][j] == 'R'):
            listlist2[i][j] = 'G'
count1 = 0
count2 = 0

def dfs(listlist,r,c,color):
    if(-1<r<n and -1<c<n):
        if(listlist[r][c] != 'N'):
            if(listlist[r][c] == color):
                listlist[r][c] = 'N'
                dfs(listlist,r-1,c,color)
                dfs(listlist,r+1,c,color)
                dfs(listlist,r,c-1,color)
                dfs(listlist,r,c+1,color)
                return 1
            return 0
        return 0
    return 0
    


for i in range(n):
    for j in range(n):
        color1 = listlist1[i][j]
        color2 = listlist2[i][j]
        count1 += dfs(listlist1,i,j,color1)
        count2 += dfs(listlist2,i,j,color2)

print(count1,count2, end= " ")

# dfs 아이디어 적용
# python의 deepCopy사용!

            
