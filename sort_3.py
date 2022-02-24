n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)

for i in range(k):
  _a = -1*(i+1)
  _b = i
  if a[_a] < b[_b]:
    a[_a], b[_b] = b[_b], a[_a]

print(sum(a))