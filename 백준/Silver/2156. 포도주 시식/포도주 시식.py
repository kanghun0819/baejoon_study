n = int(input())

arr = [0]*10001

for i in range(1,n+1):
    arr[i]=int(input())

dp = [0]*10001

dp[1]=arr[1]
if(n>=2):
    dp[2]=arr[1]+arr[2]
if(n>=3):
    dp[3]=max(arr[1]+arr[3],arr[2]+arr[3],dp[2])

if(n>=4):
    for i in range(4,n+1):
        dp[i] = max(dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i],dp[i-1])

print(max(dp))