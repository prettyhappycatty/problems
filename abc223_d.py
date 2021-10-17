#トポロジカルソート、DAG Directed Acyclic Graph

import collections
import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())

edges = []
for i in range(N):
    edges.append([])

# 始点の判定につかう入次数
indeg = [0]*N

for i in range(M):
    x, y = list(map(int, input().split()))
    edges[x-1].append(y-1)
    indeg[y-1] += 1

import heapq 
     
Q = []
 
for i in range (N):
    if indeg[i] == 0:
        heapq.heappush(Q,i)

ans = []
while Q:
    u = heapq.heappop(Q)
    ans.append(u+1)
    for v in edges[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            heapq.heappush(Q,v)

if len(ans) != N:
    print(-1)
else:
    print(*ans)