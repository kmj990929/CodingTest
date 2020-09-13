#implementation
#이것이 코딩테스트다 4-3.


start = input()
start_x = start[0]
start_y = int(start[1])

case_x = [2,2,-2,-2,1,-1,1,-1]
case_y = [-1,1,-1,1,-2,-2,2,2]

x_list = 'abcdefgh'
for i in range(len(x_list)):
  if(start_x == x_list[i]):
    start_x = i+1

count = 0
for j in range(8):
  change_x = start_x + case_x[j]
  change_y = start_y + case_y[j]
  if(change_x > 0 and change_y > 0 and change_x < 9 and change_y < 9):
    count += 1

print(count)
#07:35


