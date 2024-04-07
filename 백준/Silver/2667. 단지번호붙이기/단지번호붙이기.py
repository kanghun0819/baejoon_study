n = int(input())

arr =[]

for i in range(n):
    arr.append(input())

visited = [[0]*n for i in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]
cnt = 0
result = []

def dfs(y,x):
    global cnt
    if(visited[y][x]==1 or arr[y][x]=='0'):
        return
    if(arr[y][x]=='1'):
        cnt+=1
    for i in range(4):
        for j in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if(0<=ny<n and 0<=nx<n):
                visited[y][x]=1
                dfs(ny,nx)


for i in range(n):
    for j in range(n):
        if(arr[i][j]=='1'):
            dfs(i,j)
            if(cnt!=0):
                result.append(cnt)
                cnt=0


print(len(result))
result.sort()
for i in result:
    print(i)