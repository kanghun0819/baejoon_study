n,m = map(int,input().split())


arr = []
cnt = 0
i = 1
j=1
while j<=1001:
    temp = i
    while temp>0:
        arr.append(i)
        temp -=1
        cnt+=1
    j=cnt
    i+=1

print(sum((arr[n-1:m])))

