n = int(input())

loop = []

for i in range(n):
    loop.append(int(input()))

loop.sort(reverse=True)

result = []

for i in range(len(loop)):
     result.append(loop[i]*(i+1))
    
print(max(result))

