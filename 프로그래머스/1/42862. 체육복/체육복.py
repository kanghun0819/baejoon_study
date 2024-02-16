def solution(n, lost, reserve):


    visited = [1]*n
    answer = 0

    for i in reserve:
        visited[i-1] = 2
    for i in lost:
        if(visited[i-1]==2):
            visited[i-1]=1
        elif(visited[i-1]==1):
            visited[i-1]=0
        else:
            visited[i-1] = 0

        
    
    for i in range(n):
        if(visited[i]==1 or visited[i]==2):
            answer+=1
  
        if(visited[i]==0):
            if(i-1>=0):
                if(visited[i-1]==2):
                    visited[i-1]=1
                    visited[i]=1
                    answer+=1
                    continue

            if(i+1<n):
                if(visited[i+1]==2):
                    visited[i+1]=1
                    visited[i]=1
                    answer+=1



    return answer




