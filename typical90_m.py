#https://mirucacule.hatenablog.com/entry/2020/05/21/124026
#すぐに理解できなかった分のメモをコメント追加する

from heapq import heappush, heappop
#INF = 10 ** 9
def dijkstra(s, n): # (始点, ノード数)
    dist = [-1] * n
    hq = [(0, s)] # (distance, node)　#始点をゼロにする
    dist[s] = 0
    done = [False] * n # ノードが確定済みかどうか

    while hq:
        v = heappop(hq)[1] # ノードを pop する

        if done[v] == True:
            #print('cont')
            continue

        done[v] = True

        for to, cost in adj[v]: # 未確定のもので、注目しているノードに接続するものに距離を入力
            #print(v, to, done[to],dist[to])
            if dist[to] == -1 or dist[v] + cost < dist[to]:#すでに入力がある場合はそれより短い場合に更新
                dist[to] = dist[v] + cost 
                heappush(hq, (dist[to], to))
    return dist

# ノード数, エッジ数, 始点ノード
v, e = map(int, input().split())
# adj[s]: ノード s に隣接する(ノード, 重み)をリストで持つ
adj = [[] for _ in range(v)]
for i in range(e):
    s, t, d = map(int, input().split()) #ノード番号、ノード番号、辺重み
    adj[s-1].append((t-1, d))
    adj[t-1].append((s-1, d))

print(adj)

ans = dijkstra(0, v)
print(ans)
for i in range(1, v+1):
    if i == 1:
        #print("i=",i)
        print(ans[v-1])
    else:
        ans2 = dijkstra(i-1, v)
        print(ans2)
        print(ans[i-1]+ans2[v-1])

#print(d)