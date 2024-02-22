def solution(triangle):
    answer = 0

    array = [[] for i in range(len(triangle))]
   
    for i in range(len(array)):
        for j in range(len(triangle[i])):
            array[i].append(0)

    for i in range(1,len(array)):
        for j in range(len(array[i])):
            if(i==1):
                triangle[i][j]+=triangle[i-1][0]
            elif(j==0):
                triangle[i][j]+=triangle[i-1][j]
            elif(j==len(array[i])-1):
                triangle[i][j]+=triangle[i-1][j-1]
            else:
                triangle[i][j]+=max(triangle[i-1][j-1],triangle[i-1][j])
            

    answer = max(triangle[-1])
    return answer
