#Greedy_algorithm
#이것이 코딩테스트다 3-1. 문제1.


n,m,k = input().split()
input_list = input().split()

input_list.sort()

num = 0
sum_n = 0
count = 0
while(num < int(m)):
  if(count == int(k)):
    sum_n += int(input_list[-2])
    count = 0
  else:
    sum_n += int(input_list[-1])
    count += 1
  num += 1

print(sum_n)
