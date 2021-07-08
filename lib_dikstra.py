#https://mirucacule.hatenablog.com/entry/2020/05/21/124026
#すぐに理解できなかった分のメモをコメント追加する

# ノード数, エッジ数, 始点ノード
v, e, r = map(int, input().split())
# adj[s]: ノード s に隣接する(ノード, 重み)をリストで持つ
adj = [[] for _ in range(v)]
for i in range(e):
    s, t, d = map(int, input().split()) #ノード番号、ノード番号、辺重み
    adj[s].append((t, d))


from heapq import heappush, heappop
INF = 10 ** 9
def dijkstra(s, n): # (始点, ノード数)
    G = []
    for _ in range(0,):
    dist = [INF] * n
    hq = [(0, s)] # (distance, node)　#始点をゼロにする
    dist[s] = 0
    seen = [False] * n # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        seen[v] = True
        for to, cost in adj[v]: # 未確定のもので、注目しているノードに接続するものに距離を入力
            if seen[to] == False and dist[v] + cost < dist[to]:#すでに入力がある場合はそれより短い場合に更新
                dist[to] = dist[v] + cost 
                heappush(hq, (dist[to], to))
    return dist


print(adj)
d = dijkstra(r, v)
print(d)