N = int(input())
A = list(map(int, input().split()))

A.sort()

sumA = []
s = 0
for i in range(N):
    s += A[i]
    sumA.append(s)

#print(sumA)

ss = 0
for i in range(N):
    tmp = sumA[N-1]-sumA[i]-(N-i-1)*A[i]
    #print(tmp)
    ss += tmp

print(ss)

