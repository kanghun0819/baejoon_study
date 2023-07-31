n = int(input())
arr = []
result = []
temp = ''
cnt = 0
for i in range(n):
    arr.append(input())

for w in arr:
    for i in range(len(w)):
        if ord(w[i])>=48 and ord(w[i])<=57:
            temp +=w[i]
            cnt +=1
        else:
            if(cnt>0):
                result.append(temp)
                cnt = 0
                temp=''
    if(cnt>0):
        result.append(temp)
        cnt = 0
        temp=''

for i in range(len(result)):
    result[i] = int(result[i])
result.sort()

for i in result:
    print(i)

