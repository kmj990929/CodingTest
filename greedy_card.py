#Greedy_algorithm
#이것이 코딩테스트다 3-1. 문제2.


n, m = map(int,input().split())
lst = []
for i in range(n):
  lst_row = list(map(int,input().split()))
  lst.append(lst_row)

min_lst = []
for i in range(n):
  min_lst.append(min(lst[i]))

print(max(min_lst))

# 07:06