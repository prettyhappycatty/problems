#ワーシャルフロイド法

N, M = map(int, input().split())

INF = 10**11
dist = [[INF for _ in range(N)] for _ in range(N)]

for i in range(N):
    dist[i][i] = 0

for i in range(M):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = c


#ワーシャルフロイド本体
def wf_cnt():
    #print(dist)
    cnt = 0
    for k in range(N):
        for x in range(N):
            for y in range(N):
                dist[x][y] = min(dist[x][y], dist[x][k]+dist[k][y])
                if dist[x][y] < INF:
                    cnt += dist[x][y]
                
    return cnt
#print(dist)
#print(sm_list)

cnt = wf_cnt()
print(cnt)