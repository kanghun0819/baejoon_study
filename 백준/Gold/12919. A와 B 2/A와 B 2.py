import sys
answer = []
def dfs(string):
    if string == s:
        print(1)
        sys.exit()
    if(len(string)==0):
        return 0
    if(string[-1]=='A'):
        dfs(string[:-1])
    if(string[0]=='B'):
        dfs(string[1:][::-1])

s = list(input())
t = list(input())

dfs(t) 
print(0)