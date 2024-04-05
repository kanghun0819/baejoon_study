n,m = map(str,input().split())


arr_x = []
arr_y = []
result_arr = []
for i in n:
    arr_x.append(i)
for j in m:
    arr_y.append(j)

arr_x.reverse()
arr_y.reverse()

temp_x = ''.join(arr_x)
temp_y = ''.join(arr_y)
result = int(temp_x)+int(temp_y)

for i in str(result):
    result_arr.append(i)

result_arr.reverse()
print(int(''.join(result_arr)))