N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

s = 0
B = A*K
print(B)
for i in range(N*K):
    bi = B[i]
    for j in range(i+1, N*K):
        bj = B[j]
        if bi > bj:
            s += 1
print(s)

#TODO


