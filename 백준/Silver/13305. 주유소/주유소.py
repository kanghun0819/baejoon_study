"""
n = int(input())

distance = []
price = []
result = 0

for i in range(n-1):
    distance.append(int(input()))

for i in range(n):
    price.append(int(input()))

result +=distance[0]*price[0]
min=0
for i in range(1,n-2):
    for j in range(2,n-1):
        if(price[i] < price[j+1]):
            min = price[i]

"""
import sys

input = sys.stdin.readline
#도시 수
n = int(input())

#거리, 주유소가격
distance = list(map(int,input().split()))
oil_cost = list(map(int, input().split()))

#첫 주유소보다 기름값이 싼 주유소가 나올때까지의 거리만큼 기름넣음
paid = 0
min_cost = 1000000001
for i in range(n-1):
  if oil_cost[i] < min_cost:
    min_cost = oil_cost[i]
  paid += min_cost * distance[i]
print(paid)


    

