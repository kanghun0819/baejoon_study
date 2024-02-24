from collections import deque



def solution(operations):
    answer = []

    array = deque()

    temp = []

    for i in operations:
        temp.append(i.split(" "))
    
    
    for array_1 in temp:
        if(array_1[0]=='I'):
            array.appendleft(int(array_1[1]))
        
        elif(array_1[0]=='D'):
            if(len(array)==0):
                continue
            else:
                if(array_1[1]=='-1'):
                    array.remove(min(array))
                else:
                    array.remove(max(array))

    if(len(array)>=1):
        answer.append(max(array))
        answer.append(min(array))
    else:
        answer = [0,0]
    


    return answer
