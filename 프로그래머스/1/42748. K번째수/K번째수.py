def solution(array, commands):

    answer = []
    for array_1d in commands:
        temp = []
        a = array_1d[0]-1
        b = array_1d[1]
        c = array_1d[2]-1
        for i in range(a,b):
            temp.append(array[i])
        temp.sort()
        answer.append(temp[c])
    return answer