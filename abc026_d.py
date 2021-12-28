import math

A, B, C = map(int, input().split())

def ft(t):
    return A*t+B*math.sin(C*t*math.pi) 


N = 10**9

ok = -1.0
ng = 100.0

while abs(ok-ng) > 10**(-12):
    mid = (ok+ng) / 2.0
    #print(get_n(mid), X)
    if ft(mid) > 100:
        ng = mid
    else:
        ok = mid

print(ok)
print(100-ft(ok))