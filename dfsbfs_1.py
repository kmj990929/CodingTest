n,m = map(int, input().split())
ice_board = []
for i in range(n):
  ice_board.append(list(map(int,input())))

move_set = [(-1,0), (1,0), (0,-1), (0,1)]

def dfs(v):
  v_y, v_x = v
  if ice_board[v_y][v_x] == 1:
    return True
  ice_board[v_y][v_x] = 1
  for move in move_set:
    x = v_x + move[0]
    y = v_y + move[1]
    if x>=m or y>=n or x<=-1 or y <=-1:
      continue
    else:
      if ice_board[y][x]==0:
        dfs((y,x))
      else:
        ice_board[y][x] == 1

cnt = 0
for i in range(n):
  for j in range(m):
    result = dfs((i,j))
    if result is None:
      cnt += 1

print(cnt)