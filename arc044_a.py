import math


N = int(input())

def is_prime(n):
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

#print(eratosthenes())
if N == 1:
    print("Not Prime")
    exit()

r = is_prime(N)
#print(r)

if r:
    print("Prime")
    exit()
else:
    if N % 2 == 0 or N % 5 == 0 or N % 3 == 0:
        print("Not Prime")
    else:
        print("Prime")