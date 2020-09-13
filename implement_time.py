#implementation
#이것이 코딩테스트다 4-2.


n = int(input())

#sol1
"""
count = 0
for i in range(n+1):
  for j in range(60):
    for k in range(60):
      result = str(i)+str(j)+str(k)
      if('3' in result):
        count += 1

print(count)
"""
#5:44

#sol2
"""
m = 0
for i in range(n+1):
  if "3" in str(i):
    m +=1
print(m*3600 + (n+1-m)*(45*15+15*60))
"""
#08:03

#sol3
m = 0
if(n>10):
  m = 1
  if(n>20):
    m += 1
m += (n % 10) //3
print(m*3600 + (n+1-m)*(45*15+15*60))

