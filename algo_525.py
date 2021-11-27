#dfs

import sys
sys.setrecursionlimit(10**6)

N= int(input())
P = list(map(int, input().split()))

G = [[] for i in range(N)]
for i in range(N-1):
	G[P[i]].append(i+1)

#print(G)
ans = [0]
def search(i):
    if i == 0:
    	return
    else:
        for g in G[i]:
            ans.append(g)
            search(g)
    return

for g in G[0]:
    ans.append(g)
    search(g)

print(*ans)