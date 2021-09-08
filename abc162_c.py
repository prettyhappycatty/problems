import math
from functools import reduce
def my_gcd(*numbers):
    return reduce(math.gcd, numbers)

a = int(input())

ans = 0
for i in range(1, a+1):
    for j in range(1, a+1):
        for k in range(1, a+1):
            params = [i,j,k]
            ans += my_gcd(*params)

print(ans)