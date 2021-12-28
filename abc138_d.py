import sys
sys.setrecursionlimit(100000000)

N, Q = map(int, input().split())


G = {}
depth = [-1 for _ in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    if a-1 not in G.keys():
        G[a-1] = []
    G[a-1].append(b-1)
    if b-1 not in G.keys():
        G[b-1] = []
    G[b-1].append(a-1)

#print(G)

def countup(bef, pp):
    cnt[pp] += up[pp]
    if pp in G.keys():
        for nei in G[pp]:
            if nei == bef:
                continue
            cnt[nei] += cnt[pp]
            countup(pp,nei)
            #print(cnt)

cnt = [0 for _ in range(N)]
up = [0 for _ in range(N)]
for _ in range(Q):
    p, x = map(int, input().split())
    up[p-1] += x

#print(up)
countup(-1,0)

print(*cnt)

    