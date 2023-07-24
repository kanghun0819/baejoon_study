n = int(input())

arr = list(map(str,input().split()))

max = ""
min = ""
visites = [False]*10

def flag(i,j,k):
    if(k=='<'):
        return i<j
    else:
        return i>j

def dfs(index,string):
    global max,min

    if(index==n+1):
        if(len(min)==0):
            min =string
        else:
            max = string
        return
        
    
    for i in range(10):
        if(visites[i]==False):
            if(index==0 or flag(string[-1],str(i),arr[index-1])):
                visites[i]=True
                dfs(index+1,string+str(i))
                visites[i]=False
        
    


dfs(0,"")
print(max)
print(min)