N = int(input())

A = list(map(int, input().split()))

A_sa = [] #i+1, i 間のコスト
S_sa = [0] #0,iまでの距離の輪
sm = 0
bef = 0
for i in range(N):
    sm += abs(bef - A[i])
    bef = A[i]
sm +=abs(bef)
# 1を通らない時
# S - Sa[i]


for i in range(N):
    a = 0
    if i > 0:
        a =  A[i-1]
    b = A[i]
    c = 0
    if (i != N - 1):
        c = A[i+1]

    ans = sm
    ans -=abs(a-b)
    ans -=abs(b-c)
    ans +=abs(a-c)
    print(ans)