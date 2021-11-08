#modコンビネーション
#https://cocoinit23.com/ncr-mod-1000000007/
#nCr
from functools import reduce
def comb(n,r,mod):
    numerator = reduce(lambda x, y: x * y % mod, [n - r + k + 1 for k in range(r)])
    denominator = reduce(lambda x, y: x * y % mod, [k + 1 for k in range(r)])
    return numerator * pow(denominator, mod - 2, mod) % mod