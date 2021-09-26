plus_matrix = [[0 for _ in range(10)] for _ in range(10)]
mul_matrix = [[0 for _ in range(10)] for _ in range(10)]
MOD = 998244353

for i in range(10):
    ii = i
    for j in range(10):
        jj = j
        plus_matrix[i][j] = (ii+jj)%10
        mul_matrix[i][j] = (ii*jj)%10

N = int(input())
A = list(map(int, input().split()))

#dp[i][j] #i操作したあとに、先頭がjとなる通り数。
dp = []
for i in range(N+1):
    dp_tmp = []
    for j in range(10):
        dp_tmp.append(0)
    dp.append(dp_tmp)

dp[0][A[0]] = 1
for i in range(N-1):
    for j in range(10):
        #print("i,j=",i,j, "len=", len(dp), len(dp[0]), "alen=",len(A))
        dp[i+1][plus_matrix[j][A[i+1]]] += dp[i][j] % MOD
        dp[i+1][mul_matrix[j][A[i+1]]] += dp[i][j] % MOD

#print(dp)
for i in range(len(dp[N-1])):
    print(dp[N-1][i] % MOD)