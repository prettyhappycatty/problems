N = int(input())
MOD = 998244353

dp = [[-1 for i in range(9)] for j in range(N)]

#print(dp)
#print(dp[0][3])

#初期値 1桁目は1~9で1個ずつ
for i in range(9):
    dp[0][i] = 1

#次の桁以降は、1の場合は、1,2のものを含む。2~8のものは、+1と0と-1を足す。9の場合は8,9のみ。

for j in range(1, N):
    for i in range(0, 9):
        if i == 0:
            dp[j][i] = (dp[j-1][i] + dp[j-1][i+1]) % MOD
        elif i == 8:
            dp[j][i] = (dp[j-1][i] + dp[j-1][i-1]) % MOD
        else:
            dp[j][i] = (dp[j-1][i+1] + dp[j-1][i] + dp[j-1][i-1]) % MOD

print(sum(dp[N-1]) % MOD)

#print(dp)