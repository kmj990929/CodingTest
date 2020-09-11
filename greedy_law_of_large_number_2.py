#Greedy_algorithm
#이것이 코딩테스트다 3-1. 문제1.
# 시간복잡도 개선

n,m,k = input().split()
input_list = input().split()

input_list.sort()

first = int(input_list[-1])
second = int(input_list[-2])

result = (first*int(k) + second) * (int(m) //(int(k)+1)) + (int(m) % (int(k)+1)) * first
print(result)