M = int(input())

g = {i:[] for i in range(9)}

INF = 10**11
dist = [[INF for _ in range(9)] for _ in range(9)]

for i in range(9):
    dist[i][i] = 0

for i in range(M):
    u,v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
    dist[v-1][u-1] = 1
    dist[u-1][v-1] = 1

A = list(map(int, input().split()))



def wf_cnt():
    #print(dist)
    cnt = 0
    for k in range(9):
        for x in range(9):
            for y in range(9):
                dist[x][y] = min(dist[x][y], dist[x][k]+dist[k][y])
                if dist[x][y] < INF and dist[x][y] >=0:
                    cnt += dist[x][y]
                
    return cnt

diffs = {i:-1 for i in range(9)}
for i in range(8):
    if len(g[i]) == 0 and A[i] == i-1:
        print(-1)
        exit()
    if A[i] != i-1:
        diffs[i] = A[i]-1

print(diffs)
#ワーシャルフロイド
wf_cnt()

cnt = 0
for k in diffs.keys():
    if diffs[k] == -1:
        continue
    if dist[k][diffs[k]] == INF:
        print(-1)
        exit()
    print(k,diffs[k],dist[k][diffs[k]])
    cnt += dist[k][diffs[k]]

print(cnt)

#print(dist)
#print(A)