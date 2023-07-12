n,m = map(int,input().split())
cnt=0
while n<=m:
    if(n==m):
        print(cnt+1)
        break

    elif(m%10 == 1):
        m = m//10
        #print(m)
        cnt+=1       
    else:
        if(m%2!=0):
            break
        m = m//2
        cnt+=1
        
       # print(m)
if(n!=m):
    print(-1)
    

    

