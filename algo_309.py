N, M = map(int, input().split())

#部分和問題

A = list(map(int, input().split()))

#i番目までを選んで総和をjにできるか？
dp = [[False for _ in range(M)] for _ in range(N+1)]

dp[0][0] = True

for i in range(N):
    for j in range(M):
        if j-A[i] >= 0 and dp[i][j-A[i]] == True:
            dp[i+1][j] = True
        elif dp[i][j] == True:
            dp[i+1][j] = True

#print(dp)
if dp[N][M-2] == True:
    print("Yes")
else:
    print("No")