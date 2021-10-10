N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# DP[i][j] i番目のabc配列までで、最後がjの場合の個数
MOD = 998244353

DP = [[0 for j in range(3000+1)] for i in range(N+1)]

#初期設定
bef_sum = 0
for i in range(a[0], b[0]+1):
    DP[0][i] = 1
    bef_sum += DP[0][i]

#DP
for i in range(1, N):#N個の配列
    tmp_bef_sum = bef_sum
    bef_sum = 0
    for j in range(b[i],a[i]-1,-1):#a[i]~b[i]までのループ
        if b[i-1] <= j:
            DP[i][j] = tmp_bef_sum
        else:
            DP[i][j] = DP[i][j+1] - DP[i-1][j+1]
        #print("i,j=",i, j,"b=", b[i-1], "dp=",DP[i][j])
        bef_sum += DP[i][j]
#print(DP[N-1])
print(sum(DP[N-1]) % MOD)
