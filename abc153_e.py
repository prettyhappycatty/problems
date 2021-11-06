H, N = map(int, input().split())
A,B = [],[]
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)


#ナップサックDP
inf = 10**9
dp = [[inf for i in range(H+1)]for j in range(N+1)]
#dp[i][h] i回魔法を使った時に、HP残がhであるときの、最小の消費MP

dp[0][H] = 0

for i in range(N):
    for h in range(H,-1,-1):
        dp[i + 1][h] = min(dp[i + 1][h], dp[i][h])#魔法を使わないときの遷移
        dp[i][max(0, h - A[i])] = min(dp[i][max(0, h - A[i])], dp[i][h] + B[i])
        #魔法を使うときの遷移　h-A[i] i番目の魔法をt使ったときの残りのHP、dp[i][h] + B[i] i番目の魔法を使った時の消費MP

        #print(i,h, dp[i + 1][h], dp[i][h])
#print(dp)
print(dp[N][0])