n = int(input())

cnt5=0
cnt2=0
result = 0
if(n%5==0):
    print(n//5)
else:
    while(5*cnt5<n):
        if((n-cnt5*5)%2==0):
            result = cnt5 + (n-cnt5*5)//2
        cnt5+=1
    if(result==0):
        print(-1)
    else:
        print(result) 



        


