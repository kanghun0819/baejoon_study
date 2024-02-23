def solution(n, results):
    answer = 0

    array = [[0]*n for i in range(n)]

    cnt=0

    for i,j in results:
        array[i-1][j-1]=1
        array[j-1][i-1]=-1

    for index in range(n):
        for i in range(n):
            for j in range(n):
                if array[i][index] ==1 and array[index][j]==1:
                    array[i][j]=1
                elif array[i][index]==-1 and array[index][j]==-1:
                    array[i][j]=-1

    
    for i in range(len(array)):
        if(array[i].count(0)==1):
            answer+=1
    
    print(answer)

    
    



    return answer