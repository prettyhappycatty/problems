#グラフアルゴリズム

N, M, X = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


distance = [-1 for i in range(N)]
distance[X] = 0

friends = set(G[X])

result = set()
for v in G[X]:
    for w in G[v]:
        # アルル自身Xと、アルルの友達friendsは除いておく
        if w != X and not w in friends:
            result.add(w)

print(len(result))