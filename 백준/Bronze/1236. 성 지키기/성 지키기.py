n,m = map(int,input().split())


array = []

for i in range(n):
    array.append(input())
#오랜만에 2차원 배열 python으로 입력 받기

cnt =0
cnt_1 =0
for i in range(n):
    if 'X' not in array[i]:
        cnt+=1

for j in range(m):
    if 'X' not in [array[i][j] for i in range(n)]:
        cnt_1 +=1

print(max(cnt,cnt_1))