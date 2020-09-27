#implementation
#이것이 코딩테스트다 4-1.

n = int(input())
lrud = input().split()

x,y = 1,1
for i in range(len(lrud)):
  current = lrud[i]
  before_x, before_y = x, y
  if(current == 'L'):
    x -= 1
  elif(current == "R"):
    x += 1
  elif(current == "U"):
    y -= 1
  elif(current == "D"):
    y += 1
  if (x*y == 0 or x > n or y > n):
    x,y = before_x, before_y

print(y,x)
#7:20
#