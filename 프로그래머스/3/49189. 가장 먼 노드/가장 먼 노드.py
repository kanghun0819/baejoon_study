from collections import deque

def solution(n, edge):
    answer = 0

    graph = [[] for i  in range(n+1)]
    visited  = [0]*(n+1)
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    queue = deque()

    queue.append(1)
    visited[1]=1

    while queue:
        current = queue.popleft()

        for check in graph[current]:
            if visited[check] ==0 :
               queue.append(check)
               visited[check] = visited[current]+1
        
    for i in visited:
        if(i==max(visited)):
            answer+=1
    
    return answer

