# 解説AC、なんでこの式でいけるのかわからん　要復習

mod = 10**9+7
N = int(input())

a = [1, 0, 0]

for i in range(3,N+1):
    a.append((a[i-1]+a[i-3])%mod)

print(a[N])