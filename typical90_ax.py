N, L = map(int, input().split())

DP = [-1] * N

for i in range(0, N):
    if i == 0:
        DP[i] = 1
    elif 0 < i < L:
        DP[i] = DP[i-1]
    else:
        DP[i] = DP[i-1]+DP[i-L]
if N < L:
    print((DP[N-1]) % (10**9+7))
else:
    print((DP[N-1]+DP[N-L]) % (10**9+7))