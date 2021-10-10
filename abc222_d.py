N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# DP[i][j] i番目のabc配列までで、最後がjの場合の個数
MOD = 998244353
frame = 3000

DP = [[0 for j in range(frame+1)] for i in range(N+1)]

#初期設定
bef_sum = 0
for i in range(a[0], b[0]+1):
    DP[0][i] = 1
    bef_sum += DP[0][i]

#DP
for i in range(1, N):#N個の配列
    bef_sum_ary = [0 for j in range(frame+1)]#累積和の配列
    for j in range(a[i-1],b[i]+1):
        bef_sum_ary[j] += (bef_sum_ary[j-1] + DP[i-1][j]) % MOD
    for j in range(a[i],b[i]+1):#a[i]~b[i]までのループ
        DP[i][j] = bef_sum_ary[j] % MOD
    #print(bef_sum_ary)

#print(DP[N-1])
print(sum(DP[N-1]) % MOD)
