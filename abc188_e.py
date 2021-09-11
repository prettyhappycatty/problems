# DAG トポロジカルソート　DP

INF = 10**9 + 5
N, M = map(int, input().split())
a = list(map(int, input().split()))
g = [[] for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    g[x-1].append(y-1)#0_index

#print(g)
dp = [INF] * N
# dp[i] 街iまでの最小の金の値段

for v in range(N):
    for next in g[v]:#接続する街に対して繰り返す
        dp[next] = min(dp[next], dp[v], a[v])#次の街での最小・今の最小・街vでの売値買い値
#print(dp)

ans = max(a[i] - dp[i] for i in range(N) if dp[i] != INF)#売値買値の差
print(ans)