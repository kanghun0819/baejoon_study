ans = 0

def solution(numbers, target):

    target

    dfs(numbers,0,0,target)
    
    return ans



def dfs(n,cnt,sum,target):
    global ans
    if cnt ==len(n):        
        if(sum == target):
            ans +=1
        return
    
    dfs(n,cnt+1,sum+n[cnt],target)
    dfs(n,cnt+1,sum-n[cnt],target)