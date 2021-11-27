import math
from functools import reduce
def my_gcd(*numbers):
    return reduce(math.gcd, numbers)

N = int(input())
A = list(map(int, input().split()))

gcd = my_gcd(*A)

print(gcd)