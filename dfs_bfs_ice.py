#dfs_bfs
#이것이 코딩테스트다 5. 문제1.


n, m = map(int, input().split())

field = []
visited = [[False]*m for i in range(n)]

for i in range(n):
  row = input()
  field.append(row)
  #field.append(list(map(int, input())))

def dfs(field, visited, v):
  x,y = v
  visited[y][x] = True
  move = [(0,1),(0,-1),(1,0),(-1,0)]
  for i in move:
    dx = x+i[0]
    dy = y+i[1]
    if(dx >= 0 and dy >= 0 and dx < m and dy < n):
      if(not visited[dy][dx] and int(field[dy][dx]) == 0):
        dfs(field,visited,(dx,dy))

count =0
for y in range(n):
  for x in range(m):
    if(not visited[y][x] and int(field[y][x]) == 0):
      count += 1
      dfs(field,visited,(x,y))

print(count)

#11:39