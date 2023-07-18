from collections import deque

n = []

for i in range(9):
    n.append(int(input()))

n.sort()


for i in range(len(n)-1):
    for j in range(1,len(n)):
        num1 = n[i]
        num2 = n[j]
        result = sum(n)-num1-num2
        if result == 100:
            n.remove(num1)
            n.remove(num2)
            break
    if(result==100):
        break
for i in range(len(n)):
    print(n[i])