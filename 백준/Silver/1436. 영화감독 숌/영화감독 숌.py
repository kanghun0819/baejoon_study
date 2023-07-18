n = int(input())

temp = 666
cnt = 0

while 1:
    if '666' in str(temp):
        cnt+=1
    if cnt == n:
        print(temp)
        break
    temp +=1