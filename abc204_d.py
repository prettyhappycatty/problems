N = int(input())
A = list(map(int, input().split()))

A = sorted(A)

#print(sorted_A)

K = 1000*100

#初期化
dp = [[False for i in range(K+1)] for j in range(N+1)]

sum_A = 0
for i in range(N+1):
    dp[i][0] = True
    if i < N:
        sum_A += A[i]

#print(dp)


for i in range(N):
    for j in range(K):
        if j - A[i] >= 0:
            dp[i + 1][j] = (dp[i + 1][j]) or (dp[i][j - A[i]])
        dp[i + 1][j] = (dp[i + 1][j]) or (dp[i][j])

if sum_A % 2 == 0:
    half = sum_A // 2
else:
    half = sum_A // 2 + 1

#for i in range(K+1):
#    if dp[N][i]:
#        print(i)

j = half
#print(half)
while dp[N][j] == False:
    j += 1

print(j)