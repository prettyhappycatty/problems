N, M = map(int, input().split())
H = list(map(int, input().split()))

INF = 10**8

g = {i:{} for i in range(N)}
joy = [-INF for i in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    u = u-1
    v = v-1
    if H[u] > H[v]:
        g[u][v] = H[u]-H[v]
        g[v][u] = (H[v]-H[u])*2
    else:
        g[u][v] = (H[u]-H[v])*2
        g[v][u] = H[v]-H[u]


#print(g)
#スタート地点はゼロ
joy[0] = 0

from collections import deque


d = deque()
d.append(0)

while d:
 v = d.popleft()
 for kk,vv in g[v].items():
    #kkはid
    #vvは楽しさの増え方
     if joy[kk] < joy[v]+vv:
       joy[kk] = joy[v]+vv
       d.append(kk)
     #print(kk,d,joy)

print(max(joy))