n,m,k=map(int,input().split())
numbers=list(map(int,input().split()))
numbers.sort()
cnt = 0
tmp = 0
while cnt <= m:
  tmp += numbers[-1]*k + numbers[-2]
  cnt += k+1
tmp -= numbers[-2]+numbers[-1]*(cnt-m-1)
print(tmp)
