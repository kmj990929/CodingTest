# p.339 특정 거리의 도시 찾기

from collections import deque

n,m,k,x = map(int, input().split())
loads = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int, input().split())
  loads[a].append(b)

visited = [False] * (n+1)

def bfs(graph, start, visited):
  global k
  answer = []
  
  queue = deque()
  queue.append((start,0))
  visited[start] = True
  while queue:
    node, cnt = queue.popleft()
    if cnt == k:
      answer.append(node)
    for _n in loads[node]:
      if not visited[_n]:
        queue.append((_n,cnt+1))
        visited[_n] = True
  return answer

answer = bfs(loads,x,visited)
if len(answer) == 0:
  print(-1)
else:
  for _a in sorted(answer):
    print(_a)