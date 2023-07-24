n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))


visited = [[0] * n for i in range(n)]

result = 0
cnt = 0
min_temp = 9999999

dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

def flag(a,b):
    for i in range(5):
        x = a+dx[i]
        y = b+dy[i]
        if(visited[x][y] == 1):
            return False
    return True

def dfs(cnt):
    global result
    global min_temp
    if(cnt==3):
        min_temp = min(min_temp,result)
        return
    
    for i in range(1,n-1):
        for j in range(1,n-1):
            if(flag(i,j)):
                for k in range(5):
                    x = i + dx[k]
                    y = j + dy[k]
                    visited[x][y]=1
                    result +=arr[x][y]

                dfs(cnt+1)

                for k in range(5):
                    x = i+dx[k]
                    y = j+dy[k]
                    visited[x][y]=0
                    result -=arr[x][y]

dfs(0)

print(min_temp)

            
                    
            




