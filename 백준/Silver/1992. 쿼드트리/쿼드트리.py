n = int(input())

temp = []
result =[]

arr = [input().strip() for _ in range(n)]

def dfs(x,y,n):
    
    global result
    temp = arr[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if temp != arr[i][j]:
                result.append("(")
                dfs(x,y,n//2)
                dfs(x,y+n//2,n//2)
                dfs(x+n//2,y,n//2)
                dfs(x+n//2,y+n//2,n//2)
                result.append(")")
                return
    
    if(temp=="1"):
        result.append("1")
        return
    elif(temp=="0"):
        result.append("0")
        return
dfs(0,0,n)
print(''.join(result))