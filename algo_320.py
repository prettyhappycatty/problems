import math

def check_prime(n):
	for i in range(2, int(math.sqrt(n))+1):
		if n % i == 0:
			return True
	return False

N = int(input())


for i in range(N, 1, -1):
	cp = check_prime(i)
	if cp == False:
		print(i)
		exit()
