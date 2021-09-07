N, K = map(int, input().split())

A = list(map(int, input().split()))

A_sorted = sorted(A, reverse=True)
#print(A_sorted)

if N <= K:
    print(0)
else:
    sumA = 0
    for i in range(K, N):
        sumA += A_sorted[i]
    print(sumA)