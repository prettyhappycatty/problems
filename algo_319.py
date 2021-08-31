import math

def check_prime(n):
	for i in range(2, int(math.sqrt(n))+1):
		if n % i == 0:
			return True
	return False

N = int(input())
cp = check_prime(N)

if N == 1:
    print("No")
elif cp == True:
    print("No")
else:
    print("Yes")