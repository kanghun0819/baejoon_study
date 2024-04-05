n = int(input())


arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))
temp = [0]*n
tmp = 0
cnt = 0

for i in range(n):
    for j in range(n):
        for k in range(5):
            if(i==j):
                break
            if(arr[i][k]==arr[j][k]):
                cnt+=1
                break
    if(cnt>=temp[i]):
        temp[i]=cnt
        cnt=0
    else:
        cnt=0
print(temp.index(max(temp))+1)

