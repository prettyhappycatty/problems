N, M =  map(int, input().split())

A = list(map(int,input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)

#print(A)
#print(B)

i = 0
j = 0
minAB = 10**9+1
while i < N and j < M:
    tmp = abs(A[i]-B[j])
    if A[i]-B[j] > 0:
        j += 1
    else:
        i += 1
    if minAB > tmp:
        minAB = tmp

print(minAB)
