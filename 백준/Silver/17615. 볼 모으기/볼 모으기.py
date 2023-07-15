n = int(input())

arr = input()
r =0
b =0

flag  = False
cnt = 0

for i in range(n):
    if(flag==False):
        if(arr[-1-i]=='R'):
            continue
        else:
            flag=True
    elif(flag==True):
        if(arr[-1-i]=='R'):
            r+=1

flag = False
for i in range(n):
    if(flag==False):
        if(arr[-1-i]=='B'):
            continue
        else:
            flag=True
    elif(flag==True):
        if(arr[-1-i]=='B'):
            b+=1

print(min(b,r))


