H, W = map(int, input().split())
A = []
for i in range(H):
    tmpA = list(map(int, input().split()))
    A.append(tmpA)

#print(A)

for i1 in range(H-1):
    for i2 in range(i1+1,H):
        for j1 in range(W-1):
            for j2 in range(j1+1, W):
                if A[i1][j1] + A[i2][j2] > A[i1][j2] + A[i2][j1]:
                    print("No")
                    exit()

print("Yes")