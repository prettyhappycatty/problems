N, M = map(int, input().split())

A = []
dp = [-1 for _ in range(N+1)]
dp[0] = 1

for i in range(M):
   tmp = int(input())
   A.append(tmp) 
   dp[tmp] = 0



if dp[1] != 0:
    dp[1] = 1


for i in range(2, N+1):
    if dp[i] != 0:
        dp[i] = (dp[i-1]+dp[i-2]) % (10**9+7)

#print(dp)

print(dp[N])