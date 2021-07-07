import math

N, K = map(int, input().split())

def eratosthenes(n):
    ret = [i for i in range(1, n+1)]
    ret2 = [0]*n
    for i in range(1, N):
        if ret[i] > 0:
            j = ret[i]
            ret2[j-1] += 1
            while 1:
                j += ret[i]
                if j-1 >= n:
                    break
                ret[j-1] = -1
                ret2[j-1] += 1
    return ret, ret2

ret1, ret2 = eratosthenes(N)

#print(ret1)
#print(ret2)
cnt = 0
for i in range(N):
    if ret2[i] >= K:
        cnt += 1 
print(cnt) 
