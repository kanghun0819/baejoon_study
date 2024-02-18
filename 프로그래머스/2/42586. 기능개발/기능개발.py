from collections import deque
import time

def solution(progresses, speeds):
    answer = [0]*len(progresses)
    start = 0
    day = 0
    cnt = 0
    queue = deque()

    flag =False

    while start < len(progresses):
        if(flag==False):
            if(progresses[start]<100):
                progresses[start]+=speeds[start]
                day+=1
            else:
                flag=True
                answer[cnt]+=1
                start+=1
        else:
            if(progresses[start]+speeds[start]*day<100):
                cnt+=1
                flag=False
                progresses[start]+=speeds[start]*day
            else:
                answer[cnt]+=1
                start+=1

    result = []

    for i in answer:
        if(i==0):
            break
        else:
            result.append(i)
  
    return result

