import math

N = int(input())
A = list(map(int, input().split()))

def eratosthenes(n):
	ret = [i for i in range(1, n+1)]
	for i in range(1, math.floor(math.sqrt(n))+1):
		if ret[i] > 0:
			j = ret[i]
			while 1:
				j += ret[i]
				if j-1 >= n:
					break
				ret[j-1] = -1
	ret2 = []
	for i in range(1, len(ret)):
		if ret[i] > -1:
			ret2.append(ret[i])
	return ret2


candidate = eratosthenes(1001)

max_cnt = 0
for i in range(len(candidate)):
    cnt = 0
    for j in range(len(A)):
        if A[j] % candidate[i] == 0:
            cnt += 1
    if max_cnt <= cnt:
        ans = candidate[i]
        max_cnt = cnt
        #print(ans)

print(ans)