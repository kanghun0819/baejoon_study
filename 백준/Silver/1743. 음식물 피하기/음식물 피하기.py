import sys
sys.setrecursionlimit(10**5)
n,m,k = map(int,input().split())

arr = [[0 for j in range(m+1)]for i in range(n+1)]

for i in range(k):
    a,b = map(int,input().split())
    arr[a][b]='#'

dx = [0,0,-1,1]
dy = [1,-1,0,0]

cnt = 0
result = 0
visited = [[0 for j in range(m+1)] for i in range(n+1)]


def dfs(y,x):
    global cnt

    for i in range(4):
        nx = x +dx[i]
        ny = y +dy[i]
        if(ny>=0 and ny<=n and nx >=0 and nx<=m):
            if(visited[ny][nx]==0):
                if(arr[ny][nx]=='#'):
                    visited[ny][nx]=1
                    cnt+=1
                    dfs(ny,nx)



for i in range(n+1):
    for j in range(m+1):
        if(visited[i][j]==0):
            if(arr[i][j]=='#'):
                cnt = 0
                dfs(i,j)
                result = max(result,cnt)

print(result)










