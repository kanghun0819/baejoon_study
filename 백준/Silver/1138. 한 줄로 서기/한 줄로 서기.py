n = int(input())
arr = list(map(int, input().split()))
sub_arr = [0] * n
for i in range(1, n+1):
    temp = arr[i-1]
    cnt = 0
    for j in range(n):
        if cnt == temp and sub_arr[j] == 0:
            sub_arr[j] = i
            break
        elif sub_arr[j] == 0:
            cnt += 1
for i in sub_arr:
    print(i,end=' ')