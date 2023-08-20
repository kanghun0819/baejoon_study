n,c = map(int,input().split())

arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()
warr = []
count = 0 
start = 1
end = arr[-1] - arr[0]
result = 0
while start <=end:
    middle = (start + end)//2
    temp = arr[0]
    count = 1
    for i in range(1,len(arr)):
        if (arr[i]>=temp + middle):
            temp = arr[i]
            count+=1
    if(count>=c):
        start = middle +1
        result = middle
    else:
        end = middle -1

print(result)





    


