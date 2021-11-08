#くり返し二乗法

def ppow(x, n, MOD):
    res = 1
    if n > 0:
        res = ppow(x, n//2, MOD)
        if n % 2 == 0:
            res = (res*res) % MOD
        else:
            res = ((res*res) % MOD*x) % MOD
    return res


print(ppow(2,10,100))

#pow(x,n,MOD)でくり返し２乗法してくれるw