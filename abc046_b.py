N, K = list(map(int, input().split()))

mul = K
for i in range(1, N):
    mul *= (K-1)

print(mul)
