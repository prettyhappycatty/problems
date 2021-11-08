N, A, B = map(int, input().split())

MOD = 10**9+7
from functools import reduce
#nCr
def comb(n,r,mod):
    numerator = reduce(lambda x, y: x * y % mod, [n - r + k + 1 for k in range(r)])
    denominator = reduce(lambda x, y: x * y % mod, [k + 1 for k in range(r)])
    return numerator * pow(denominator, mod - 2, mod) % mod

ans = pow(2, N, MOD) - 1 - comb(N,A,MOD) - comb(N,B,MOD)
print(ans % MOD)