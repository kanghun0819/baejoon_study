from collections import deque

n,k = map(int,input().split())

visited = [0]*1000001

q = deque()
q.append(n)
while q:
    x = q.popleft()
    if( x == k):
        print(visited[x])
        break
    else:
        for i in [x-1,x+1,2*x]:
            if 0<=i and i <1000001 and not visited[i]:
                visited[i] = visited[x]+1
                q.append(i)
    

