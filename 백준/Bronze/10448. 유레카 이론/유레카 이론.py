t = []
answer = [0]*1001
result = []
for i in range(1,45):
    t.append((i*(i+1))//2)

n = int(input())

for i in range(n):
    result.append(int(input()))

for i in t:
    for j in t:
        for k in t:
            if i+j+k <=1000:
                answer[i+k+j]=1
for i in result:
    print(answer[i])

