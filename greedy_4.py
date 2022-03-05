n,k = map(int, input().split())
cnt = n%k + int(n**(1/k))
print(cnt)