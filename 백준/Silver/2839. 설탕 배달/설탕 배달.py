n = int(input())


cnt5=0
cnt3=0

while n>0:
    if(n%5==0):
        cnt5 = n//5
        n = n-5*cnt5
    else:
        cnt3+=1
        n = n-3
if(n<0):
    print(-1)
else:
    print(cnt5+cnt3)
