N = int(input())
A = list(map(int, input().split()))

#A = sorted(A)
K = 1000*100

#初期化
dp = [[False for i in range(K+1)] for j in range(N+1)]
#何も選ばず合計0は全てTrue
for i in range(N+1):
    dp[i][0] = True


for i in range(N):
    for j in range(K):#合計Kまで1つずつインクリメント
        if j - A[i] >= 0:#合計j - A[i]がTrueならA[i]を選択すればTrueになる。もしくは、すでにdp[i+1][j]にTrueが入ってればTrue。
            dp[i + 1][j] = (dp[i + 1][j]) or (dp[i][j - A[i]])
        #選択しなければ、dp[i][j]がTrueもしくは、すでにdp[i+1][j]にTrueが入ってればTrue。
        dp[i + 1][j] = (dp[i + 1][j]) or (dp[i][j])