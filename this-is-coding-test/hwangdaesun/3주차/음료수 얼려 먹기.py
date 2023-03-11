n,m = map(int,(input().split()))
# n이 행, m이 열

graph = [list(map(int,input()))for _ in range(n)]
print(graph)

r = 0
c = 0
count = 0

# 0이면 1로 바꿔 그리고 return 1 
# 1이면                return 0
# 제한

def dfs(graph,r,c):
    if(-1<r<n and -1<c<m):
        if(graph[r][c] == 0):
            graph[r][c] = 1
            dfs(graph,r+1,c)
            dfs(graph,r-1,c)
            dfs(graph,r,c+1)
            dfs(graph,r,c-1)
            return 1
        return 0    
    

for i in range(n):
    for j in range(m):
        count += dfs(graph,i,j)
print(count)
            





