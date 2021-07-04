H, W = map(int, input().split())

A = []
B = []

for i in range(H):
    tmpA = list(map(int, input().split()))
    A.append(tmpA)

for i in range(H):
    tmpB = list(map(int, input().split()))
    B.append(tmpB)

def change(i,j):
    diff = B[i][j] - A[i][j]
    A[i][j] += diff 
    A[i][j+1] += diff 
    A[i+1][j] += diff 
    A[i+1][j+1] += diff 
    return abs(diff)
#print(A)
#print(B)

cnt = 0
for i in range(H-1):
    for j in range(W-1):
        cnt += change(i,j)

for i in range(H):
    if A[i][W-1] != B[i][W-1]:
        print("No")
        exit()

for j in range(W):
    if A[H-1][j] != B[H-1][j]:
        print("No")
        exit()

print("Yes")
print(cnt)
