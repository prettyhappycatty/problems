import math

N = int(input())

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
    ret[0] = -1 #1を素数から除く
    return ret 

erato = eratosthenes(100000)

#その数までの素数の個数を持っておく
prime_sum = [0]
psum = 0
for i in range(100000):
    if i > 1 and erato[i] != -1 and erato[(i+1)//2] != -1:
        psum += 1
    prime_sum.append(psum)

#print(prime_sum)

for i in range(N):
    tmp_a, tmp_b = map(int, input().split())
    tmp_a, tmp_b = tmp_a-1, tmp_b-1 
    #print(tmp_a, tmp_b, prime_sum[tmp_a], prime_sum[tmp_b+1],prime_sum[tmp_b+1]-prime_sum[tmp_a])
    print(prime_sum[tmp_b+1]-prime_sum[tmp_a])


