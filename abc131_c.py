import math

A, B, C, D = map(int, input().split())

#ほうじょ原理？

def divcnt(n, c, d):
    #n以下の数でCで割り切れるものの個数
    nc = n // c
    nd = n // d
    ncd = n//(c*d//math.gcd(c,d))
    ans = n - (nc + nd - ncd)
    #print(n,":", c, "で割れる個数", nc, d, "で割れる個数", nd, c*d, "で割れる個数", ncd, "->", ans)
    return ans

print(divcnt(B, C, D)-divcnt(A-1, C, D))