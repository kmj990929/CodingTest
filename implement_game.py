#implementation
#이것이 코딩테스트다 4-4.


n,m = map(int, input().split())

a,b,d = map(int, input().split())

game_map = []
for i in range(n):
  game_map.append(list(map(int, input().split())))
game_map[a][b] = 1

count = 1
case = [(-1,0),(0,1),(1,0),(0,-1)]
check = 0
while True:
  if (d > 0):
    d-= 1
  else:
    d = 3

  change_a = a+case[d][0]
  change_b = b+case[d][1]
  check += 1
  if(game_map[change_a][change_b] == 0):
    a = change_a
    b = change_b
    game_map[a][b] = 1
    count += 1
    check = 0
    print(a,b)
  elif(check == 4):
    change_a = a+case[(d+2)%4][0] # a-case[d][0]
    change_b = b+case[(d+2)%4][1] # b-case[d][1]
    if(game_map[change_a][change_b] == 0):
      a = change_a
      b = change_b
      game_map[a][b] = 1
      count += 1
      check = 0
    else:
      break

print(count)
#19:07    

