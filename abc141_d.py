import heapq

N, M = map(int,input().split())

def mul_minus(s):
    return -int(s)


A = list(map(mul_minus, input().split()))

heapq.heapify(A)

for i in range(M):
    p = heapq.heappop(A)
    pp = (-p)//2
    heapq.heappush(A, -pp)

print(-sum(A))
