import math

def eratosthenes():
	n = 100
	ret = [i for i in range(1, n+1)]
	for i in range(1, 6):
		if ret[i] > 0:
			j = ret[i]
			while 1:
				j += ret[i]
				if j-1 >= n:
					break
				ret[j-1] = -1
	
	cnt = 0
	for i in range(6, int(math.sqrt(n))+1):
		if ret[i] > 0:
			j = ret[i]
			while 1:
				j += ret[i]
				if j-1 >= n:
					break
				if ret[j-1] > -1:
					cnt += 1
				ret[j-1] = -1
	return cnt

print(eratosthenes())