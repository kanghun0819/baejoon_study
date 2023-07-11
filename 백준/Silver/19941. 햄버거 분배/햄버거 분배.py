n,k = map(int,input().split())

arr = list(input())
cnt = 0
result = 0 
for i in range(len(arr)):
    if(arr[i] == 'P'):
        for j in range(-k,k+1):
            if(j+i in range(n)):
                if(arr[i+j]=='H'):
                    cnt+=1
                    arr[i+j]='X'
                    break

print(cnt)

