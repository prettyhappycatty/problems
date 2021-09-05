import math
from functools import reduce
def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


N, X = map(int, input().split())

A = list(map(int, input().split()))
A.sort()
#print(A)

diff = []

for i in range(N):
    diff.append(abs(A[i]-X))

#print(diff)
print(my_gcd(*diff))