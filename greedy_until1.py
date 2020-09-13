#Greedy_algorithm
#이것이 코딩테스트다 3-1. 문제3.

n, k = map(int,input().split())

#sol1.
num = 0
while(n!=1):
  if(n % k == 0):
    n = n//k
  else:
    n -= 1
  num += 1

print(num)
#2:31

#sol2.
"""
num = 0
while(n!=1):
  if(n%k==0):
    num += 1
    n = n//k
  else:
    num += n % k
    n -= n % k

print(num)  
"""
#6:8

