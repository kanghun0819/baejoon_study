n = input().split('-')

result = 0
for i in n[0].split('+'):
    result += int(i)
for j in n[1:]:
    for k in j.split('+'):
        result -=int(k)

print(result)
