N, K, A = map(int, input().split())

if N == 1:
    print(1)
    exit()

if A+K < N:
    print(A+K-1)
else:
    a = (A + K - 1) % N
    if a == 0:
        print(N)
    else:
        print(a)