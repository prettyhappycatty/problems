import math

def is_eratosthenes(n):
    ret = [i for i in range(1, n+1)]
    if n == 1:
        return "No"
    for i in range(1, math.floor(math.sqrt(n))+1):
        if ret[i] > 0:
            j = ret[i]
            while 1:
                j += ret[i]
                if j-1 >= n:
                    break
                ret[j-1] = -1

    if len(ret) == 0:
        return "No"
    elif ret[len(ret)-1] == n:
        return "Yes"
    else:
        return "No"

N = int(input())
print(is_eratosthenes(N))




