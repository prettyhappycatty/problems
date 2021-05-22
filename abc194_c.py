N = int(input())
A = list(map(int, input().split()))

kou1 = 0
kou2 = 0
for i in range(N):
    kou1 += A[i]*A[i]
    kou2 += A[i]

print(N*kou1-kou2**2)
