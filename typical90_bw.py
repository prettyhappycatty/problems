import math

N = int(input())
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

#print(ary)
ary = prime_factorize(N)
#print(ary2)

cnt = 0
a = 1
while a < len(ary):
    a *= 2
    cnt += 1
print(cnt)


