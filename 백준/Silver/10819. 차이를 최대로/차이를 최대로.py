n = int(input())

arr = list(map(int,input().split()))

stack = [] 
result = []
visited =[0]*n

def dfs(i):
    if(len(stack)==n):
        temp = cal(stack)
        result.append(temp)
        return
    for i in range(len(arr)):
        if(visited[i]==0):
            stack.append(arr[i])
            visited[i]=1
            dfs(i+1)
            stack.pop()
            visited[i]=0

def cal(array):
    temp = 0 
    for i in range(len(array)-1):
        temp+=abs(array[i]-array[i-1])
    return temp
dfs(0)
print(max(result))