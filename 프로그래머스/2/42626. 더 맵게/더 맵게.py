import heapq

def solution(scoville, K):
    cnt = 0 
    heapq.heapify(scoville)
    temp = scoville[0]
    while 1:
        if(temp<K):
            if len(scoville)==1:
                return -1
            else:
                a = heapq.heappop(scoville)
                b = heapq.heappop(scoville)
                temp = a + 2*b
                heapq.heappush(scoville,temp)
                temp = scoville[0]
                cnt+=1

        else:
            break
    
    return cnt

