def solution(participant, completion):
    answer = ''

    array = dict()
    

    for i in participant:
        if i in array:
            array[i] +=1
        else:
            array[i] = 1


    for i in completion:
        if i in array:
            array[i]-=1
        
    for i in array.keys():
        if(array[i]==1):
            answer +=i
            return i


