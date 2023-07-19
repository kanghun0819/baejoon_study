from collections import deque
n,m = map(int,input().split())



array = list(map(int,input().split()))

cnt = 0

result = []
temp = deque()



def back(a,b):
    global cnt
    global array
    if(a==n):
        return
    if(b+array[a]==m):
        cnt+=1
    
    back(a+1,b)
    back(a+1,b+array[a])

back(0,0)

print(cnt)




