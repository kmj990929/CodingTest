n = int(input())
answer = []
for i in range(n):
  answer.append(int(input()))

for j in sorted(answer, reverse=True):
  print(j, end=" ")