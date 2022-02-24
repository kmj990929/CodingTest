n = int(input())
score = []
for i in range(n):
  score.append(tuple(input().split()))

score.sort(key=lambda x:x[1])
for j in score:
  print(j[0], end=' ')
