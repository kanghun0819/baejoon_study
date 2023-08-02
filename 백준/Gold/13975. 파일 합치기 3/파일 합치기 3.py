from collections import deque
import heapq
t =int(input())

cnt = 0
result = 0
cal = []
summer = []
while cnt <t:
    n = int(input())
    arr = list(map(int,input().split()))
    heapq.heapify(arr)
    
    result = 0
    while len(arr)>1:
            b = heapq.heappop(arr)
            c = heapq.heappop(arr)
            temp= b+c
            result+=temp
            heapq.heappush(arr,temp)
    cnt+=1
    print(result)
    


        



