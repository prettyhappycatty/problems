N, K = map(int, input().split())


import heapq
S = []
for i in range(N):
    tmpS = input()
    S.append(tmpS)

heapq.heapify(S)
bef = heapq.heappop(S)
for i in range(1,K):
    b = heapq.heappop(S)
    heapq.heappush(S, bef+b)
    bef = heapq.heappop(S)

print(heapq.heappop(S))