#ナップサック問題
#N 個数　W重さ

N, W = map(int, input().split())

WW = []
VV = []
for i in range(N):
	w, v = map(int, input().split())
	WW.append(w)
	VV.append(v)

dp = [[0 for _ in range(W+1)] for _ in range(N+1)] #Wを超えない
for j in range(W):
    dp[0][j] = 0
#print(WW)

for i in range(N):
	#i番目を選ぶ時
    for j in range(W+1):
        if j-WW[i]  >= 0:
            dp[i+1][j] = max(dp[i][j-WW[i]] + VV[i], dp[i][j])
        else:
        #選ばない時
            dp[i+1][j] = dp[i][j]
print(dp[N][W])