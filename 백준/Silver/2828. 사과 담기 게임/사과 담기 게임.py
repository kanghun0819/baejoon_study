n,m = map(int,input().split(" "))
count = int(input())



location = []

cnt =0
result = 0
start = 0

subarr = []

for i in range(1,21):
    subarr.append(i)




for i in range(count):
    location.append(int(input()))
for i in location:
    #if(i in subarr[start:m]):
     #   print(cnt)
    if(i not in subarr[start:m]):
        if(i<m):
            while 1:
                if(i in subarr[start:m]):
                    break
                start -=1
                m -=1
                cnt +=1
        elif(i>m):
            while 1:
                if(i in subarr[start:m]):
                    break
                start +=1
                m +=1
                cnt +=1


print(cnt)
     


