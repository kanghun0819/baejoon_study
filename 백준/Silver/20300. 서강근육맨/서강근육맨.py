n = int(input())

arr = list(map(int,input().split()))

max = 0 
arr.sort()
if(len(arr)%2!=0):
    for i in range(n//2):
        if(max<arr[i]+arr[n-i-2]):
            max = arr[i]+arr[n-i-2]
    if(max<arr[-1]):
        max = arr[-1]
else:
    for i in range(n//2):
        if(max<arr[i]+arr[n-i-1]):
            max = arr[i]+arr[n-i-1]
print(max)
    

