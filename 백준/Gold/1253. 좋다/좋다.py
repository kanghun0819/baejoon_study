n = int(input())

arr = list(map(int,input().split()))

arr.sort()
cnt = 0
def binary_search(left,right,target,index):
    global cnt
    while left < right:
        if(left == index):
            left+=1
        elif(right ==index):
            right -=1
        elif((arr[left]+arr[right]) == target):
            cnt+=1
            return 
        elif((arr[left] + arr[right])>target):
            right -=1
        elif(arr[left]+arr[right]<target):
            left+=1
    #     binary_search(left,right-1)
    # else:
    #     binary_search(left+1,right)
for i in range(len(arr)):
    binary_search(0,len(arr)-1,arr[i],i)
print(cnt)