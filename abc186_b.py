H, W = map(int, input().split())

A = []
sm = 10**3
for i in range(H):
    tmpA = list(map(int, input().split()))
    A.append(tmpA)
    for j in range(W):
        if tmpA[j] < sm:
            sm = tmpA[j]

sm2 = 0
for i in range(H):
    for j in range(W):
        sm2 += A[i][j]-sm

print(sm2)