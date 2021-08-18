import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()] # nは頂点の数、mは辺の数
g = [[] for _ in range(n)] # 隣接リスト

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

from collections import deque

cnt = [0]
d_min = [10**9]

#print(g)
def bfs(u):
    queue = deque([u])
    cnt = 0
    d = [-1] * n # uからの距離の初期化
    d[u] = 0 # 自分との距離は0
    sm = -1
    while queue:
        v = queue.popleft()
        #print(g[v])
        for i in g[v]:
            if d[i] == -1:
                d[i] = d[v]+1
                if i == n-1 and sm == -1:
                    cnt += 1
                    sm = d[i]
                elif i == n-1:
                    cnt += 1
                queue.append(i)
                print(sm, cnt)
            elif d[i] == sm:
                cnt += 1
            else:
                print(i,d[i])
        print(d)
    return d, cnt


# 0からの各頂点の距離
d,c = bfs(0)
#print(d)
print(c)