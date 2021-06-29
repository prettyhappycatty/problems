import math



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
    print(ret) 

eratosthenes(1000)