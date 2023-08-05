n = int(input())
m = int(input())

arr = list(map(int,input().split()))

arr.sort()
i = 0 

j = len(arr)-1

cnt = 0
while i<j:
    if(arr[i]+arr[j]==m):
        cnt +=1
        i+=1
        j-=1
    elif(arr[i]+arr[j]<m):
        i+=1
    elif(arr[i]+arr[j]>m):
        j-=1
print(cnt)
    