import heapq

N, M = map(int, input().split())

A, B, C = [], [], []
G = []
for _ in range(0, N):
    G.append([])

prize_sum = 0
for _ in range(M):
    c, u, v = map(int, input().split())

    G[u-1].append((v-1, c))
    G[v-1].append((u-1, c))
    prize_sum += c

#print(G)
# プリム法　最小全域木
marked = []

for _ in range(0, N):
    marked.append(False)

marked_count = 0

# 最初の点を選んでマーク
marked[0] = True
marked_count += 1

# 次に選ぶ点のheap
Q = []
for j, c in G[0]:
    heapq.heappush(Q, (c,j))

tree_sum = 0

while marked_count < N:

    #print(marked_count, Q)
    c, i = heapq.heappop(Q)

    if marked[i]:
        continue

    marked[i] = True
    marked_count += 1

    tree_sum += c
    #print(i, c)
    
    for (j, c) in G[i]:
        if marked[j]:
            continue
        
        heapq.heappush(Q, (c,j))

print(prize_sum-tree_sum)