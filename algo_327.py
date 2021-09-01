import math

def eratosthenes():
	n = 30
	ret = [i for i in range(1, n+1)]
	for i in range(1, 4):
		if ret[i] > 0:
			j = ret[i]
			while 1:
				j += ret[i]
				if j-1 >= n:
					break
				ret[j-1] = -1
	
	for i in range(4, int(math.sqrt(30))+1):
		if ret[i] > 0:
			j = ret[i]
			while 1:
				j += ret[i]
				if j-1 >= n:
					break
				#ret[j-1] = -1
				if ret[j-1] > -1:#合成数だったreturn
					return ret[j-1]
	return ret

print(eratosthenes())