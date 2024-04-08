from collections import deque
import math

n = int(input())
stack = []
result = []
temp = []

# 소수 판별 함수


def dfs(i):
    if(is_prime_number(int(i))==False or i in temp):
        
        return
    if(len(i)==n and is_prime_number(int(i))):
        result.append(i)
        
        return
    for j in range(1,10):
        temp.append(i)
        dfs(i+str(j))
        temp.pop()

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

dfs('2')
dfs('3')
dfs('5')
dfs('7')

for i in result:
    print(int(i))
