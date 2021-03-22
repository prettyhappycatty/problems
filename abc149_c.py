
import math
s = int(input())

def check_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        #print(n,i, n % i)
        if n % i == 0:
            return True
    return False

while check_prime(s):
    s += 1
    #print(s)
    #if s > 1000:
    #    break

print(s)