

N = int(input())
A = []


ans = 0
sumn = [0]*N
#print(sumn)
for i in range(N):
    tmpA = list(map(int,input().split()))
    for j in range(6):
        sumn[i] += tmpA[j]
    A.append(tmpA)

mul = 1
for s in sumn:
    mul *= s

print(mul % (10**9+7))

