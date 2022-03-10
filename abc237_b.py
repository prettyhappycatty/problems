H, W = map(int, input().split())

A = []

for i in range(H):
    tmpa = list(map(int, input().split()))
    A.append(tmpa)

#print(A)

for i in range(W):
    b = []
    for j in range(H):
        b.append(A[j][i])
    print(*b)