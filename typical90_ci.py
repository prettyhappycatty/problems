import copy

N, P, K = map(int, input().split())

INF = 10**8+1
A = []
# ワーシャルフロイドの準備、全体をINF、同じ頂点同士を0とする
dist = [[INF for _ in range(N)] for _ in range(N)]
sm_list = [] 
cnt_st_k = N*N

for i in range(N):
    tmpA = list(map(int, input().split()))
    A.append(tmpA)

#ワーシャルフロイド本体
def wf_cnt(n):
    for x in range(N):
        for y in range(N):
            if A[x][y] == -1:
                #print(n)
                dist[x][y] = n
            else:
                dist[x][y] = A[x][y]
    #print(dist)
    for k in range(N):
        for x in range(N):
            for y in range(N):
                dist[x][y] = min(dist[x][y], dist[x][k]+dist[k][y])
    cnt = 0
    for x in range(N):
        for y in range(x+1, N):
            if dist[x][y] >= P:
                cnt += 1
    #print(dist, cnt)
    print(dist, P)
    print(cnt)
    return cnt
#print(dist)
#print(sm_list)





def solve(tmp):
    left = 1
    right = 10**9
    minx = 10**9
    while right -left > 1:
        mid = (left+right) // 2
        v = wf_cnt(mid)
        if v <= P:
            right = mid
            minx = min(minx, mid)
        else:
            left = mid

    return right


#for i in range(200):
    #print(wf_cnt(i))

L = solve(K)
R = solve(K+1)
print(L, R)
if R > N*N:
    print("Infinity")
elif L > N*N:
    print(0)
else:
    print(R-L)

#print(A)
