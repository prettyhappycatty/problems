
from heapq import heappush, heappop

N, M = map(int, input().split())

G = []
for _ in range(0,N):
    G.append([])


U = []
V = []
C = []

for _ in range(0,M):
    u, v, c = map(int, input().split())
    G[u-1].append((v-1,c))
    #G[v-1].append((u-1,c))

#print(G)

def dijkstra(s, n): # (始点, ノード数)
    dist = [-1] * n
    Q = [] # (distance, node)　#始点をゼロにする

    heappush(Q, (0, s))
    dist[s] = 0

    done = [False] * N
    while len(Q) > 0:
        d, i = heappop(Q) # ノードを pop する

        if done[i]:
            continue

        done[i] = True

        for j, c in G[i]: # 未確定のもので、注目しているノードに接続するものに距離を入力
            #print(G, dist[i], dist[j], c)
            if dist[j] < 0 or dist[i] + c < dist[j]:#すでに入力がある場合はそれより短い場合に更新
                dist[j] = dist[i] + c
                heappush(Q, (dist[j], j))
    return dist

r = 1
#print(adj)

for i in range(0, v):
    ans = dijkstra(0, v)
    if i == 0:
        #print("i=",i)
        print(ans[v-1])
    else:

        #print("i=",i)
        #ans = dijkstra(0, v)
        print(ans[v-1])
        ans2 = dijkstra(i, v-1)
        print(ans2)
        print(ans[i-1]+ans2[v-1])

#print(d)