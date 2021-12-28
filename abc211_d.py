import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()] # nは頂点の数、mは辺の数
g = [[] for _ in range(n)] # 隣接リスト

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    g[a-1].append(b-1)
    g[b-1].append(a-1)

from collections import deque

cnt = [0]


#print(g)
def bfs(u):
    queue = deque([u])
    d = [-1] * n # uからの距離の初期化
    cnt = [0] * n # uからの距離の初期化
    cnt[0] = 1
    d[u] = 0 # 自分との距離は0
    sm = -1 #最初に出てくるものが一番短い
    while queue:
        v = queue.popleft()
        #print(g[v])
        for i in g[v]:
            if d[i] == -1:#距離がまだ決まっていない時
                d[i] = d[v]+1
                cnt[i] = cnt[v] 
                queue.append(i)
            elif d[i] == d[v]+1:
                cnt[i] += cnt[v]
                cnt[i] %= 10**9+7
    return d, cnt


# 0からの各頂点の距離
d,c = bfs(0)
#print(d)
print(c[n-1])