N = int(input())

def div46(s):
    return int(s) % 46

A = list(map(div46, input().split()))
B = list(map(div46, input().split()))
C = list(map(div46, input().split()))

#print(A)

divA = {}
divB = {}
divC = {}

for i in range(N):
    if A[i] not in divA.keys():
        divA[A[i]] = 0
    if B[i] not in divB.keys():
        divB[B[i]] = 0
    if C[i] not in divC.keys():
        divC[C[i]] = 0
    divA[A[i]] += 1
    divB[B[i]] += 1
    divC[C[i]] += 1

sumPtn = 0
for ak in divA.keys():
    for bk in divB.keys():
        for ck in divC.keys():
            if (ak+bk+ck) % 46 == 0:
                sumPtn += divA[ak]*divB[bk]*divC[ck]
print(sumPtn)



