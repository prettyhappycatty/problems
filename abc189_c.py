N = int(input())
A = list(map(int, input().split()))

#区間最小値を求めておく
#dp = [[-1 for _ in range(N)] for _ in range(N)]
#for i in range(N):
#    dp[i][i] = A[i]
#    for j in range(i+1, N):
#         dp[i][j] = dp[i][j-1] + min(A[j]-dp[i][j-1], 0)
# print(dp)

#l, r の組を全探索

INF = 10**10
sq_max = 0
for l in range(N):
    min_A = INF
    for r in range(l, N):
        min_A = min(min_A, A[r])
        sq_max = max(sq_max, min_A*(r-l+1))
        #print(l, r, min_A, (r-l+1), sq_max)

print(sq_max)