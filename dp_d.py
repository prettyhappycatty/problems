N, W = map(int, input().split())
# 6 15
# 価値 重さ
# 1 5

# dp[i][j]i:価値の総和,j:重さの総和

dp = [[-1 for _ in range(W+1)] for _ in range(N+1)]
for w in range(W):
    dp[0][w] = 0

for i in range(N):
    w_tmp, v_tmp = map(int, input().split())
    for w in range(W+1):
        if w >=w_tmp:
            dp[i+1][w] = max(dp[i][w-w_tmp] + v_tmp, dp[i][w])
        else:
            dp[i+1][w] = dp[i][w]

print(dp[N][W])
