from collections import deque
n = int(input())
arr = []
start=[]
link = []

visit = [0]*n
cnt = 0
results = 0
resultl = 0
min_teemp = 99999
temp = 0
total =0
for i in range(n):
    arr.append(list(map(int,input().split())))



def flag(i):
    if(visit[i]==1):
        return False
    else:
        return True
    
count = 0

def dfs(k,cur):
    global start
    global results
    global resultl
    global min_teemp
    global temp
    global total
    global count
    temps = 0
    templ = 0
    for i in range(k,n):
        if(cur==n//2):
            for i in range(n//2):
                for j in range(i,len(start)):
                    temps+=arr[start[i]][start[j]]+arr[start[j]][start[i]]
            for i in range(n):
                if i not in start:
                    link.append(i)
            for i in range(len(link)-1):
                for j in range(i,len(link)):
                    templ += arr[link[i]][link[j]]+arr[link[j]][link[i]]
                    #print(result)
            #print(start,link)
            results = temps
            resultl = templ
            temp = abs(results-resultl)
            min_teemp = min(temp,min_teemp)
            link.clear()
            return
        
        elif(flag(i)):
            visit[i]=1
            start.append(i)
            dfs(i,cur+1)
            start.pop()
            visit[i] = 0


dfs(0,0)
print(min_teemp)
