import math

def ff(a):
    if a == 0:return 0
    if a == 1:return 1
    if a % 2 == 0:
        a = a - 1
    return ff(math.floor(a/2.0))+ff(math.ceil(a/2.0))

print(ff(1000))