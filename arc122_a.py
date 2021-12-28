N = int(input())
A = list(map(int, input().split()))
MOD = 10**9+7

dp = [[0 for _ in range(2)] for _ in range(N)]#良い式が何通りあるか
ans = [[0 for _ in range(2)] for _ in range(N)]

# dp[0][1]
dp[0][0] = 1 # それまでの通り数
ans[0][0]= A[0] # それまでの和

for i in range(1,N):
    dp[i][0] += dp[i-1][0] + dp[i-1][1]%MOD
    dp[i][1] += dp[i-1][0]
    ans[i][0] = (ans[i-1][0]+A[i]*dp[i-1][0] + ans[i-1][1]+A[i]*dp[i-1][1])%MOD
    ans[i][1] = (ans[i-1][0]-A[i]*dp[i-1][0])%MOD

#print(ans)
#print(dp)
print(sum(ans[N-1])%MOD)


