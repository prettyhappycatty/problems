N, M = map(int, input().split())
X = list(map(int, input().split()))

X.sort()

sa = []

for i in range(M-1):
    sa.append(X[i+1]-X[i])

print(sa)
print(X)