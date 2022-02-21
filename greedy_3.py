n,m = map(int, input().split())
min_nums = []
for i in range(n):
  row = list(map(int, input().split()))
  min_nums.append(min(row))
print(max(min_nums))
