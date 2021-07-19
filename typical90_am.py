import sys
sys.setrecursionlimit(1000000000)


N = int(input())

neighbors = {}
A = []
B = []

for i in range(N-1):
    tmpA, tmpB = map(int, input().split())
    A.append(tmpA-1)
    B.append(tmpB-1)
    if tmpA-1 not in neighbors.keys():
        neighbors[tmpA-1] = []
    if tmpB-1 not in neighbors.keys():
        neighbors[tmpB-1] = []

    neighbors[tmpA-1].append(tmpB-1)
    neighbors[tmpB-1].append(tmpA-1)

#print(neighbors)

dp = [-1 for _ in range(N)] 

def dfs(pos, pre):
    dp[pos] = 1
    for i in neighbors[pos]:
        #print(dp)
        if i != pre:
            dfs(i, pos)
            dp[pos] += dp[i]

dfs(0, -1)

#print(dp)
ans = 0
for i in range(N-1):
    r = min(dp[A[i]], dp[B[i]])
    ans += r * (N - r)

print(ans)


