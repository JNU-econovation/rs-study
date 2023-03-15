import sys
sys.setrecursionlimit(10 ** 6)

t = int(input())


def dfs(graph,r,c):
    if(-1<r<n and -1<c<m):
        if(graph[r][c] == 1):
            graph[r][c] = 0
            dfs(graph,r-1,c)
            dfs(graph,r+1,c)
            dfs(graph,r,c+1)
            dfs(graph,r,c-1)
            return 1
        return 0
    return 0


for tt in range(t): #t번 반복

    m,n,k = map(int,input().split())
    count = 0

    graph = [[0 for i in range(m)] for _ in range(n)]

    for kk in range(k):
        c, r = map(int,input().split())
        graph[r][c] = 1
    
    for nn in range(n):
        for mm in range(m):
            count += dfs(graph,nn,mm)
    print(count)

# DFS 적용
# 파이썬의 기본 재귀 한도가 1000이다.
# 하지만, 