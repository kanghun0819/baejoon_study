n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))
n = 5
cnt = 0
for i in arr:
    while n<=i:
        if(i//n<=0):
            break
        else:
            cnt+=i//n
            n=n*5
    print(cnt)
    cnt = 0
    n =5

            