test_chat = input()

test_chat = test_chat.upper()
array = dict()

for i in test_chat:
    if(i in array.keys()):
        array[i]+=1
    else:
        array[i]=1
reuslt = [k for k,v in array.items() if max(array.values())==v]

if(len(reuslt)>1):
    print("?")
else:
    print(reuslt[0])

