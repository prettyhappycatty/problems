N = int(input())

#300x300x300 のDP
#dp[n][taiyaki][takoyaki] = count
lunch = []

goal_taiyaki, goal_takoyaki = map(int, input().split())
for i in range(N):
    taiyaki, takoyaki = map(int, input().split())
    lunch.append(tuple((taiyaki, takoyaki)))

size = 300
#size = 10

dp = [[[10**9 for _ in range(size+1)] for _ in range(size+1)] for _ in range(size+1)]

#0個選ぶ時、お弁当の個数は0個
dp[0][0][0] = 0
#print(dp[0][0][0])

for i in range(1,len(lunch)+1):
    taiyaki, takoyaki = lunch[i-1]
    #print(taiyaki, takoyaki)
    for j in range(size+1):
        for k in range(size+1):
            jj = min(goal_taiyaki, j+taiyaki)
            kk = min(goal_takoyaki,k+takoyaki)
            #print(i-1, j, k, i, jj, kk)
            dp[i][jj][kk] = min(dp[i-1][j][k] + 1, dp[i][jj][kk]) #選ぶ時
            dp[i][j][k] = min(dp[i-1][j][k], dp[i][j][k]) #選ばない時
            #print(dp[i-1][j][k]+1, dp[i][jj][kk])
          
    #print(dp[i+1][0:10])

if dp[N][goal_taiyaki][goal_takoyaki] == 10**9:
    print(-1)
else:
    print(dp[N][goal_taiyaki][goal_takoyaki])

