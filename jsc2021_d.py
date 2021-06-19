N, P = map(int, input().split())
MOD = 1000000007
ans = (P - 1) * pow(P - 2, N - 1, MOD) % MOD
print(ans)