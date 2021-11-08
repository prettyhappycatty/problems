#グラフアルゴリズム

M, N = map(int, input().split())
G = [[] for _ in range(M)]

for i in range(N):
    a,b = map(int, input().split())
    G[a].append(b)
    #1方向のフォロー

for i in range(M):
    G[i].sort()
    ans = G[i]
    print(*ans)