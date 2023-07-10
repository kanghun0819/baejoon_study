n = int(input())
arr = list(map(int,input().split()))
arr.sort()
result = 0
for i in range(n-1):
    result +=arr[i]/2

result +=arr[-1]

print(result)
