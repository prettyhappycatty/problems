TMP = input().split()
N = int(TMP[0])
M = int(TMP[1])
X = int(TMP[2])

A = [int(x) for x in input().split()]

#print(A)

start = N
goal_X = X
goal_0 = 0

cost0 = 0
for i in range(X+1):
    if X-i in A:
        cost0 += 1  
    if X-i == 0:
        break

costN = 0
for j in range(N-X):
    if (X + j) in A:
        costN += 1  
    if j == N:
        break

if costN > cost0:
    print(cost0)
else:
    print(costN)