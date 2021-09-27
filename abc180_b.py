import math

N = int(input())
a = list(map(int, input().split()))

manh = 0
euc = 0
cheb = 0

for i in range(N):
    manh += abs(a[i])
    euc += a[i]**2
    cheb = max(cheb,abs(a[i]))

print(manh)
print(math.sqrt(euc))
print(cheb)