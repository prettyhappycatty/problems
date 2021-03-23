import math
from functools import reduce
def my_gcd(*numbers):
    return reduce(math.gcd, numbers)

N = int(input())
A = list(map(int, input().split()))

gcd = my_gcd(*A)
#print(gcd)

def divs(n):
    cnt = 0
    a = n
    while a % 2 == 0:
        cnt += 1
        a = int(a/2)
    return cnt
        
print(divs(gcd))