#Greedy_algorithm
#이것이 코딩테스트다 3-1.

n = 1260
coin_list = [500,100,50,10]

total = 0
for i in coin_list:
  num = n // i
  total += num
  n -= i*num

print(total)