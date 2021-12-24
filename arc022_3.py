import sys
sys.setrecursionlimit(1000000)

N = int(input())
A = []
B = []
g = [[] for _ in range(N)]

visited = [10**5+1 for _ in range(N)]

for i in range(N-1):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)
    g[a-1].append(b-1)
    g[b-1].append(a-1)

def dfs(i): #点iからの距離をメモ
    for j in g[i]:
        if visited[j] < 10**5+1:
            continue
        visited[j] = visited[i]+1
        dfs(j)

visited = [10**5+1 for _ in range(N)]
visited[0] = 0
dfs(0)
max_dist = 0
max_idx = -1
for i in range(len(visited)):
    if visited[i] > max_dist:
        max_dist = visited[i]
        max_idx = i 

visited = [10**5+1 for _ in range(N)]
visited[max_idx] = 0
dfs(max_idx)
#print(visited)
max_dist_2 = 0
max_idx_2 = -1
for i in range(len(visited)):
    if visited[i] > max_dist_2:
        max_dist_2 = visited[i]
        max_idx_2 = i 

print(max_idx+1, max_idx_2+1)
