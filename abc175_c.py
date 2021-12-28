X, K, D = map(int, input().split())

for i in range(K):
    if X <= 0:
        X = X + D
    else:
        X = X - D

print(abs(X))