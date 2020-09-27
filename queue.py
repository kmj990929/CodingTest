#queue
#이것이 코딩테스트다 5.


from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
print(queue)
queue.popleft()
print(queue)
queue.append(1)
queue.append(4)
queue.popleft()

queue.reverse()
print(queue)