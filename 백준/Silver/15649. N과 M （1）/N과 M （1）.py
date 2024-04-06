n,m = map(int,input().split())

visited = [0]*n

stack = []

def dfs(i):
    if(len(stack)==m):
        for i in stack:
            print(i,end=' ')
        print()
        return
    
    for i in range(n):
        if(visited[i]==0):
            stack.append(i+1)
            visited[i]=1
            dfs(i+1)
            stack.pop()
            visited[i]=0
    

dfs(0)