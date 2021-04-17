D, N = list(map(int, input().split()))

a = 100**(D)

if N == 100:
    print(a*(N+1))
else:
    print(a*N)