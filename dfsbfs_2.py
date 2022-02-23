from collections import deque

n,m = map(int, input().split())
maze = []
for i in range(n):
  maze.append(list(map(int,input())))

move_set = [(-1,0), (1,0), (0,-1), (0,1)]

def bfs(x,y):
  cnt = 0
  queue = deque([(x,y)])
  maze[y][x] = 0
  while queue:
    cursor = queue.popleft()
    if cursor[0] == m-1 and cursor[1] == n-1:
      return cnt
    check = False
    for move in move_set:
      _x = cursor[0]+move[0]
      _y = cursor[1]+move[1]
      if _x >= m or _y >= n or _x <= -1 or _y <=-1:
        continue
      elif maze[_y][_x]==1:
        queue.append((_x, _y))
        maze[_y][_x] = 0
        check=True
    if check:
      check=False
      cnt +=1

print(bfs(0,0))