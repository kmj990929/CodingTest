#dfs_bfs
#이것이 코딩테스트다 5. 문제2.

from collections import deque

n,m = map(int, input().split())

field = []
visited = [[False]*m for _ in range(n)]
for i in range(n):
  row = list(map(int, input()))
  field.append(row)

def bfs(field, visited, start):
  global count,n,m
  x,y = start
  queue = deque([start])
  visited[y][x] = True
  move = [(-1,0),(1,0),(0,1),(0,-1)]

  while queue:
    count += 1

    for _ in range(len(queue)):
      x,y = queue.popleft()
      if ((x,y) == (m-1,n-1)):
        return 0

      for i in move:
        dx = x + i[0]
        dy = y + i[1]
        if (dx >=0 and dy >= 0 and dx < m and dy < n):
          if (not visited[dy][dx] and field[dy][dx] == 1):
            queue.append((dx,dy))
            visited[dy][dx] = True

count = 0
bfs(field, visited, (0,0))
print(count)

#27:03