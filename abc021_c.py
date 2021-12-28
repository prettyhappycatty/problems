import sys
sys.setrecursionlimit(1000000)

from heapq import heappop, heappush

MOD = 10**9 + 7

N = int(input())
a, b = map(int, input().split())
M = int(input())

g = [[] for _ in range(N)]

for i in range(M):
    x, y = map(int, input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)

#print(g)
#ダイクストラ法で最短距離を求める
def dijkstra(s):
    hq = [(0, s)] #始点
    dist = [10**9+7] * N
    dist[s] = 0 #始点の距離
    seen = [False] * N #通ったかどうか
    cnt = [0] * N
    cnt[s] = 1
    while hq:
        _, v = heappop(hq)
        if seen[v]:
            continue
        seen[v] = True
        for i in g[v]:
            if dist[i] > dist[v] + 1:
                dist[i] = dist[v] + 1
                heappush(hq, (dist[i], i))
                cnt[i] = cnt[v] #初めて最短距離になる場合
            elif dist[i] == dist[v] + 1:
                cnt[i] += cnt[v] #すでに最短がある場合
                cnt[i] %= MOD
    return cnt, dist
 
cnt, dist = dijkstra(a-1)
print(cnt[b-1]%MOD)