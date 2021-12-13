A, B, X = map(int, input().split())

def get_n(n):
    return A*n+B*int(len(str(n)))

N = 10**9

ok = -1
ng = N+1

while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    #print(get_n(mid), X)
    if get_n(mid) > X:
        ng = mid
    else:
        ok = mid

#print(ok,ng)
if ok == -1:
    print(0)
else:
    print(ok)