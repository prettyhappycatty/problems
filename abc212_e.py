N, M, K = map(int, input().split())
mod = 998244353

# dp[i][j] := i日目に都市jにいる場合の数
dp = [[0 for _ in range(0,N+1)] for _ in range(0,K+1)]
dp[0][1] = 1

uv = {}
for i in range(N+1):
    uv[i] = []

for i in range(M):
    tmpU, tmpV = map(int, input().split())
    uv[tmpU].append(tmpV)
    uv[tmpV].append(tmpU)

            
for i in range(0,K):
    #print(dp[i])
    pre_sum = sum(dp[i])
    for t in range(1,N+1):
        ex = 0
        for s in uv[t]:#つながってないに含まれる分をひく
            ex += dp[i][s]
        ex += dp[i][t]
        dp[i+1][t] = pre_sum - ex
        dp[i+1][t] %= mod
 
print(dp[K][1])