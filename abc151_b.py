N, K, M = map(int, input().split())
A = list(map(int, input().split()))

sumA = 0
for i in range(N-1):
    sumA += A[i]

if N*M - sumA > K:
    print(-1)
elif N*M <= sumA:
    print(0)
else:
    print(N*M - sumA)