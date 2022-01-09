#priority_queue

import heapq 

N, K = map(int, input().split())

P = list(map(int, input().split()))

#最初の配列を0からKまでのソート済みにする
a = P[0:K]
heapq.heapify(a)

print(min(a))

for i in range(K, N):
    #一番小さいものをpop
    p = heapq.heappop(a)
    #次の配列を挿入する場合に、一番小さいものより大きいかどうかを判定、大きい方をpとする
    p = max(p, P[i])
    #大きい方をキューに戻す
    heapq.heappush(a,p)
    #最小値が答えになるのでpop
    ans = heapq.heappop(a)
    print(ans)
    #もう一度戻す
    heapq.heappush(a, ans)


